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
"""Get a key."""
from bk_bscp.client import BscpClient

SERVER_ADDRS = ["example.com:9090"]
TOKEN = "your_token"
BIZ_ID = 1


def get_key():
    with BscpClient(SERVER_ADDRS, TOKEN, BIZ_ID) as client:
        pair = client.get("app1", "key1")
        print(pair)


def get_key_with_labels():
    """Get a key with labels specified."""
    #
    # Method 1: set labels when initializing the client.
    with BscpClient(SERVER_ADDRS, TOKEN, BIZ_ID, labels={"region": "shenzhen", "env": "stag"}) as client:
        pair = client.get("app1", "key1")
        print(pair)

        # Method 2: set labels when calling the get method, the labels will overwrite
        # the client's labels if they have the same key.
        #
        # client.get("app1", "key1", labels={"env": "prod"})


def main():
    get_key()


if __name__ == "__main__":
    main()
