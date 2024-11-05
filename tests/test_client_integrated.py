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
"""The integrated tests for bk_bscp module, **a real server is required for running
these tests.**
"""

import os
from dataclasses import dataclass
from typing import List

import pytest

from bk_bscp.client import BscpClient
from bk_bscp.exceptions import BscpClientConnectionError, BscpClientGetError


@dataclass
class ClientConfig:
    """The configuration for initializing the client."""

    server_addrs: List[str]
    token: str
    biz_id: int


@pytest.fixture
def config() -> ClientConfig:
    """Read client configs from environment variables."""
    _server_addrs = os.getenv("BSCP_SERVER_ADDRS")
    if not _server_addrs:
        pytest.skip("Must set BSCP_SERVER_ADDRS to run the tests")
    server_addrs = _server_addrs.split(",")

    token = os.getenv("BSCP_TOKEN", "")
    biz_id = int(os.getenv("BSCP_BIZ_ID", "0"))
    return ClientConfig(server_addrs=server_addrs, token=token, biz_id=biz_id)


@pytest.fixture
def existent_app_key() -> List[str]:
    """An real app and key that exists in the server."""
    app_key = os.getenv("BSCP_EXISTENT_APP_KEY")
    if not app_key:
        pytest.skip("Must set BSCP_EXISTENT_APP_KEY to run the tests")
    return app_key.split(",")


class TestBscpClient:
    """Test the client class."""

    def test_init(self, config: ClientConfig):
        client = BscpClient(server_addrs=config.server_addrs, token=config.token, biz_id=config.biz_id)
        client.close()

    def test_init_failed_short_timeout(self, config: ClientConfig):
        """Use an extremely short timeout."""
        with pytest.raises(BscpClientConnectionError):
            _ = BscpClient(
                server_addrs=config.server_addrs, token=config.token, biz_id=config.biz_id, connect_timeout=0.00001
            )

    def test_init_failed_bad_server(self, config: ClientConfig):
        with pytest.raises(BscpClientConnectionError):
            _ = BscpClient(
                # An invalid server address
                server_addrs="localhost:0",
                token=config.token,
                biz_id=config.biz_id,
            )

    def test_get(self, config: ClientConfig, existent_app_key: List[str]):
        with BscpClient(server_addrs=config.server_addrs, token=config.token, biz_id=config.biz_id) as client:
            app, key = existent_app_key
            pair = client.get(app, key)
        assert pair.key == key
        assert pair.value is not None

    def test_get_non_exists(self, config: ClientConfig, existent_app_key: List[str]):
        # Try out best to forge an invalid key
        app, key = existent_app_key
        with BscpClient(
            server_addrs=config.server_addrs, token=config.token, biz_id=config.biz_id
        ) as client, pytest.raises(BscpClientGetError):
            _ = client.get(app, key + "-non-existent-suffix-for-test")


class TestBscpClientWatch:
    def test_normal(self, config: ClientConfig, existent_app_key: List[str]):
        client = BscpClient(server_addrs=config.server_addrs, token=config.token, biz_id=config.biz_id)
        app = existent_app_key[0]
        for event_obj in client.watch(app=app, timeout=1):
            print("Event:", event_obj)

        # Test watch forever
        # for event_obj in client.watch_forever(app=app):
        #     print(event_obj)
