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
"""Watch kv typed app(s) for new releases."""
import logging

from bk_bscp.client import BscpClient, WatchedApp

SERVER_ADDRS = ["example.com:9090"]
TOKEN = "your_token"
BIZ_ID = 1


def watch_app():
    """Watch a single app."""
    with BscpClient(SERVER_ADDRS, TOKEN, BIZ_ID) as client:
        for ev in client.watch_forever(app="app1"):
            _print_event_obj(client, ev)


def watch_apps():
    """Watch multiple apps at once."""
    with BscpClient(SERVER_ADDRS, TOKEN, BIZ_ID) as client:
        for ev in client.watch_apps_forever(WatchedApp(app="app1"), WatchedApp(app="app2")):
            _print_event_obj(client, ev)


def watch_apps_without_reconnect():
    """Watch multiple apps at once, do not reconnect on connection errors."""
    with BscpClient(SERVER_ADDRS, TOKEN, BIZ_ID) as client:
        # It also accept an optional "timeout" parameter
        for ev in client.watch_apps(WatchedApp(app="app1"), WatchedApp(app="app2"), timeout=1):
            _print_event_obj(client, ev)


def watch_with_labels():
    """Examples of watching with labels, there are 3 ways to set labels."""
    # Method 1: set labels when initializing the client.
    #
    with BscpClient(SERVER_ADDRS, TOKEN, BIZ_ID, labels={"region": "shenzhen", "env": "stag"}) as client:
        # Method 2: set labels when calling the watch/watch_forever method, the labels will overwrite
        # the client's labels if they have the same key.
        #
        for ev in client.watch_forever(app="app1", labels={"env": "prod"}):
            _print_event_obj(client, ev)

        # Method 3: set labels for each app when calling the watch_apps/watch_apps_forever method.
        #
        # for ev in client.watch_apps(
        #     WatchedApp(app="app1", labels={"env": "prod"}),
        #     WatchedApp(app="app2", labels={"env": "prod"}),
        #     timeout=1,
        # ):
        #     _print_event_obj(client, ev)


def _print_event_obj(client, ev):
    for key in ev.key_infos:
        value = client.get(ev.app, key.key)
        print(f"New release received, app: {ev.app}, key: {key.key}, value: {value}")


def setup_logger():
    """Set up the logger to print logs."""
    logger = logging.getLogger("bk_bscp")
    logger.setLevel("DEBUG")

    formatter = logging.Formatter("[%(asctime)s] %(name)s:%(levelname)s: %(message)s")
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)


setup_logger()


if __name__ == "__main__":
    watch_app()
    # watch_multiple_apps()
    # watch_apps_without_reconnect()
