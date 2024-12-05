# TencentBlueKing is pleased to support the open source community by making
# 蓝鲸智云 - PaaS 平台 (BlueKing - PaaS System) available.
# Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
# Licensed under the MIT License (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
#     http://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions and
# limitations under the License.
#
# We undertake not to change the open source license (MIT license) applicable
# to the current version of the project delivered to anyone in the future.
"""The client for bscp feed-server"""

import json
import logging
import random
import threading
import time
import uuid
from dataclasses import asdict, dataclass
from typing import Dict, Iterable, List, Literal, Optional, Sequence, Tuple, Union

import grpc
from typing_extensions import TypeAlias

from bk_bscp.constants import CURRENT_API_VERSION, DEFAULT_CONNECT_TIMEOUT, MessagingType, MetadataKey, WatchEventType
from bk_bscp.exceptions import (
    BscpClientConnectionError,
    BscpClientGetError,
    BscpClientHandshakeError,
    BscpClientWatchBounceError,
    BscpClientWatchError,
)
from bk_bscp.grpc_lib.core.base import base_pb2
from bk_bscp.grpc_lib.feed_server import feed_server_pb2, feed_server_pb2_grpc
from bk_bscp.models import AppOptions, KeyValuePair, KeyValueUpdatedEvent, Release, WatchAppInputParams
from bk_bscp.utils import get_fingerprint

logger = logging.getLogger("bk_bscp")

# The type for labels
Labels: TypeAlias = Dict[str, str]
# The type for request metadata
ReqMetadata: TypeAlias = List[Tuple[str, str]]


@dataclass
class WatchedApp:
    """A param type for client.watch_apps() method.

    :param app: The app name.
    :param labels: The labels, default to None.
    :param release_id: The release id, default to 0.
    """

    app: str
    labels: Optional[Dict[str, str]] = None
    release_id: int = 0


class BscpClient:
    """The client for bscp feed-server.

    :param server_addrs: The server address, can be a string or a list of addresses.
    :param token: The token for authentication.
    :param biz_id: The business id.
    :param labels: The default labels.
    :param connect_timeout: The timeout for connecting to the server, units: seconds, default: 3.
    """

    # The max backoff time for watch apps forever, unit: seconds
    default_watch_backoff_max = 120

    def __init__(
        self,
        server_addrs: Union[Sequence[str], str],
        token: str,
        biz_id: int,
        labels: Optional[Labels] = None,
        connect_timeout: float = DEFAULT_CONNECT_TIMEOUT,
    ):
        # Transform single server address to a list
        self.server_addrs: Sequence[str]
        if isinstance(server_addrs, str):
            self.server_addrs = [server_addrs]
        else:
            self.server_addrs = server_addrs

        self.token = token
        self.biz_id = biz_id
        self.labels = labels or {}
        self.connect_timeout = connect_timeout
        if self.connect_timeout <= 0:
            self.connect_timeout = DEFAULT_CONNECT_TIMEOUT

        self._fingerprint = get_fingerprint()
        # Resources should be recycled after use
        self.stub: feed_server_pb2_grpc.UpstreamStub
        self.channel: grpc.Channel
        self.stub_type: Literal["default", "keepalive"]
        self.create_default_stub()

    def create_default_stub(self):
        """Create the stub object with default channel options."""
        # Do a handshake to verify the connection
        self.stub_type = "default"
        self.stub, self.channel = self.get_upstream_stub()
        self.do_handshake()

    def create_keepalive_stub(self):
        """Re-create the stub with a channel that enables keep-alive settings. This is useful
        when the connection needs to be maintained for a long period of time.
        """
        # Close the old connection
        self.close()

        self.stub_type = "keepalive"
        # See: https://github.com/grpc/grpc/blob/master/examples/python/keep_alive/greeter_client.py
        self.stub, self.channel = self.get_upstream_stub(
            extra_options=[
                ("grpc.keepalive_time_ms", 10000),
                ("grpc.keepalive_timeout_ms", 5000),
                ("grpc.keepalive_permit_without_calls", 1),
                ("grpc.http2.max_pings_without_data", 2),
            ]
        )
        self.do_handshake()

    def do_handshake(self):
        """Do a handshake with the server to validate the connection.

        :raises BscpClientHandshakeError: If handshake failed.
        """
        msg = feed_server_pb2.HandshakeMessage(
            api_version=CURRENT_API_VERSION,
            spec=feed_server_pb2.SidecarSpec(
                biz_id=self.biz_id,
                version=base_pb2.Versioning(
                    # NOTE: Use CURRENT_API_VERSION here currently, this may change in the future
                    Major=CURRENT_API_VERSION.Major,
                    Minor=CURRENT_API_VERSION.Minor,
                    Patch=CURRENT_API_VERSION.Patch,
                ),
            ),
        )

        try:
            response = self.stub.Handshake(msg, metadata=self._get_req_metadata())
        except grpc.RpcError as e:
            raise BscpClientHandshakeError("Unable to handshake", e) from e
        logger.debug("Handshake success, api_version: %s", response.api_version)

    def pull_kvs(self, app: str, match: List[str], app_options: Optional[AppOptions] = None) -> Release:
        """Pull key-value Release from the server.
        :param app: The app name.
        :param match: The key.
        :param app_options: the app option params.
        :return: A kv Release.
        :raises BscpClientGetError: If get failed.
        """
        total_labels = {**self.labels}
        uid = self._fingerprint

        if app_options is not None:
            uid = app_options.uid
            total_labels = {**self.labels, **(app_options.labels or {})}

        msg = feed_server_pb2.PullKvMetaReq(
            match=match,
            biz_id=self.biz_id,
            app_meta=feed_server_pb2.AppMeta(
                uid=uid,
                app=app,
                labels=total_labels,
            ),
        )
        try:
            response = self.stub.PullKvMeta(msg, metadata=self._get_req_metadata())
        except grpc.RpcError as e:
            raise BscpClientGetError(f'Unable to get "{app}" release, details: {e.details()}', e) from e

        r = Release(
            release_id=response.release_id,
            kvs=response.kv_metas,
        )
        return r

    def get(self, app: str, key: str, labels: Optional[dict] = None) -> KeyValuePair:
        """Get a key-value pair from the server.

        :param app: The app name.
        :param key: The key.
        :param labels: The labels, optional, it will be merged with the client's labels
            before sending.
        :return: A key-value pair.
        :raises BscpClientGetError: If get failed.
        """
        total_labels = {**self.labels, **(labels or {})}
        msg = feed_server_pb2.GetKvValueReq(
            key=key,
            biz_id=self.biz_id,
            app_meta=feed_server_pb2.AppMeta(
                # NOTE: Use fingerprint as uid currently
                uid=self._fingerprint,
                app=app,
                labels=total_labels,
            ),
        )
        try:
            response = self.stub.GetKvValue(msg, metadata=self._get_req_metadata())
        except grpc.RpcError as e:
            raise BscpClientGetError(f'Unable to get "{key}", details: {e.details()}', e) from e
        return KeyValuePair(key=key, type=response.kv_type, value=response.value)

    def watch_forever(self, app: str, labels: Optional[dict] = None, release_id: int = 0, **kwargs):
        """Watch an app for new releases, see `.watch()` for details.

        * This method features "auto-reconnect" logic.
        """
        return self.watch_apps_forever(WatchedApp(app, labels, release_id), **kwargs)

    def watch_apps_forever(self, *watched_apps: WatchedApp) -> Iterable[KeyValueUpdatedEvent]:
        """Watch a list of apps for new releases, see `.watch_apps()` for details.

        * This method features "auto-reconnect" logic.
        """
        consecutive_errors_cnt = 0
        while True:
            try:
                yield from self.watch_apps(*watched_apps, recreate_conn=True)
            except (
                BscpClientConnectionError,
                BscpClientHandshakeError,
                BscpClientWatchBounceError,
                BscpClientWatchError,
            ) as e:
                # Increase the backoff time each time an error occurs
                backoff_seconds = min(self.default_watch_backoff_max, 2**consecutive_errors_cnt)
                consecutive_errors_cnt += 1

                logger.info("An error occurred while watching, retry in %s seconds, details: %s.", backoff_seconds, e)
                time.sleep(backoff_seconds)
                continue
            else:
                consecutive_errors_cnt = 0

    def watch(self, app: str, labels: Optional[dict] = None, release_id: int = 0, **kwargs):
        """Watch an app for new releases. Only kv type is supported at this moment."""
        return self.watch_apps(WatchedApp(app, labels, release_id), **kwargs)

    def watch_apps(
        self, *watched_apps: WatchedApp, timeout: float = 0, recreate_conn: bool = False
    ) -> Iterable[KeyValueUpdatedEvent]:
        """Watch a list of apps for new releases. Only kv type is supported at this moment.

        :param *watched_apps: The apps to be watched.
        :param timeout: The max timeout in seconds, default to 0, which means no timeout.
        :param recreate_conn: Whether to recreate the connection before starting watch, default to False.
        :return: An iterable of KeyValueUpdatedEvent.
        :raises BscpClientWatchBounceError: If the server has been bounced.
        :raises BscpClientWatchError: If there is an error watching.
        """
        # Replace the current channel/stub with one that enables keep-alive for better stability
        if self.stub_type != "keepalive" or recreate_conn:
            self.create_keepalive_stub()

        # Build the input params
        apps_input_params = []
        for w in watched_apps:
            total_labels = {**self.labels, **(w.labels or {})}
            p = WatchAppInputParams(
                app=w.app, uid=self._fingerprint, labels=total_labels, currentReleaseID=w.release_id
            )
            apps_input_params.append(p)

        # Prepare the request object
        payload = {"bizID": self.biz_id, "apps": [asdict(p) for p in apps_input_params]}
        payload_bytes = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        msg = feed_server_pb2.SideWatchMeta(api_version=CURRENT_API_VERSION, payload=payload_bytes)

        streamed_resp = self.stub.Watch(msg, metadata=self._get_req_metadata())
        # Start background tasks:
        #
        # - the heartbeat loop to keep connection active
        # - the timeout keeper to stop the watch process on time
        self._start_heartbeat_loop(streamed_resp, apps_input_params)
        if timeout > 0:
            self._start_timeout_keeper(streamed_resp, timeout)

        try:
            for event in streamed_resp:
                logger.debug(
                    "Received new event, api_version: %s, rid: %s, payload length: %s.",
                    repr(str(event.api_version)),
                    event.rid,
                    len(event.payload),
                )
                # TODO: Check API version
                if event.type == WatchEventType.Bounce.value:
                    raise BscpClientWatchBounceError("server bounce")

                elif event.type == WatchEventType.PublishRelease.value:
                    parsed_payload = json.loads(event.payload)
                    release_meta = parsed_payload["releaseMeta"]
                    if release_meta["kvMetas"]:
                        event_obj = KeyValueUpdatedEvent.from_release_meta(release_meta)
                        yield event_obj
                    else:
                        logger.debug("App types other than kv are not supported yet.")
                else:
                    logger.debug("Unknown event type: %s", event.type)
                    continue
        except grpc._channel._MultiThreadedRendezvous as e:
            if e.code() == grpc.StatusCode.CANCELLED:
                # Canceled manually
                return
            raise BscpClientWatchError(streamed_resp.code(), streamed_resp.details(), exc=e)

    def _start_heartbeat_loop(self, streamed_resp, apps_input_params: List[WatchAppInputParams]):
        """Start the heartbeat loop."""
        hb_sender = HeartbeatSender(self.stub, self._get_req_metadata())
        hb_msg = HeartbeatSender.build_msg(self._fingerprint, apps_input_params)

        threading.Thread(target=hb_sender.start, args=(hb_msg,), daemon=True).start()
        streamed_resp.add_done_callback(lambda f: hb_sender.stop())

    def _start_timeout_keeper(self, streamed_resp, timeout: float):
        """Start the timeout keeper which cancel the watch stream after the given timeout."""

        def _stop_watch():
            time.sleep(timeout)
            streamed_resp.cancel()

        threading.Thread(target=_stop_watch, daemon=True).start()
        # TODO: Use "add_done_callback()" to stop the keeper

    def get_upstream_stub(
        self, extra_options: Sequence[Tuple[str, str]] = ()
    ) -> Tuple[feed_server_pb2_grpc.UpstreamStub, grpc.Channel]:
        """Get the stub for sending requests.

        :param extra_options: The extra options for creating the channel.
        :return: The stub and the channel.
        """
        channel_options = [("grpc.primary_user_agent", "bscp-sdk-python")]
        channel_options.extend(extra_options)

        target = self._get_target()
        channel = grpc.insecure_channel(target, options=channel_options)
        # Wait until the channel is ready
        try:
            grpc.channel_ready_future(channel).result(timeout=self.connect_timeout)
        except grpc.FutureTimeoutError as e:
            raise BscpClientConnectionError(f"unable to connect to {target} in {self.connect_timeout} seconds") from e

        return feed_server_pb2_grpc.UpstreamStub(channel), channel

    def close(self):
        """Close the connections."""
        logger.debug("Closing the channel connection.")
        self.channel.close()

    def _get_target(self) -> str:
        """Get the target server address."""
        # TODO: Better load-balancing support
        return random.choice(self.server_addrs)

    def _get_req_metadata(self) -> ReqMetadata:
        """Get the metadata for sending requests."""
        metadata = [(MetadataKey.SideRid.value, uuid.uuid4().hex)]

        # sidebar meta
        sidecar_meta = {"bid": self.biz_id, "fpt": self._fingerprint}
        dumped_sidecar_meta = json.dumps(sidecar_meta)
        metadata.append((MetadataKey.SidecarMeta.value, dumped_sidecar_meta))

        if self.token:
            metadata.append((MetadataKey.Authorization.value, f"bearer {self.token}"))
        return metadata

    # Implement the context manager protocol for better connection handling
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False


class HeartbeatSender:
    """A class sends heartbeat messages to keep the connection active.

    :param stub: The stub for sending heartbeat messages.
    :param metadata: The metadata used for sending messages.
    """

    def __init__(self, stub: feed_server_pb2_grpc.UpstreamStub, metadata: ReqMetadata):
        self.stub = stub
        self.metadata = metadata
        # The flag controls the sending loop
        self._should_stop = False

    def start(self, msg: feed_server_pb2.MessagingMeta, interval: float = 15):
        """Send the heartbeat message periodically to keep the connection active. When the
        connection is active, gRPC's "keepalive" mechanism will be activated and a broken
        connection will be aborted automatically.

        :param msg: The heartbeat msg.
        :param interval: The interval in seconds.
        """
        while not self._should_stop:
            time.sleep(interval)
            try:
                _ = self.stub.Messaging(msg, metadata=self.metadata)
            except grpc.RpcError as e:
                logger.warning("Error sending heartbeat, details: %s.", e)
            else:
                logger.debug("Heartbeat finished.")

    def stop(self):
        """Stop the heartbeat sender."""
        self._should_stop = True
        logger.debug("The heartbeat sender stopped.")

    @staticmethod
    def build_msg(fingerprint: str, apps_input_params: List[WatchAppInputParams]) -> feed_server_pb2.MessagingMeta:
        """Build the heartbeat message."""
        hb_payload = {"fingerprint": fingerprint, "applications": [asdict(p) for p in apps_input_params]}
        hb_payload_bytes = json.dumps(hb_payload, ensure_ascii=False).encode("utf-8")
        hb_msg = feed_server_pb2.MessagingMeta(
            api_version=CURRENT_API_VERSION,
            rid=fingerprint,
            type=MessagingType.Heartbeat.value,
            payload=hb_payload_bytes,
        )
        return hb_msg
