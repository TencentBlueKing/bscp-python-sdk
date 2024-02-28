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
"""Constants"""
from enum import Enum

from bk_bscp.grpc_lib.core.base import base_pb2

# The API version that the current SDK is using
CURRENT_API_VERSION = base_pb2.Versioning(Major=1, Minor=0, Patch=0)

# The default timeout for connecting to the server, unit: seconds
DEFAULT_CONNECT_TIMEOUT = 3


MESSAGING_TYPE = 2


class MetadataKey(Enum):
    """The key being used in the request metadata."""

    Authorization = "authorization"
    SideRid = "side-rid"
    SidecarMeta = "sidecar-meta"


class WatchEventType(Enum):
    """The event type."""

    Bounce = 1
    PublishRelease = 2


class MessagingType(Enum):
    """The type for call "messaging" API."""

    SidecarOffline = 1
    Heartbeat = 2
