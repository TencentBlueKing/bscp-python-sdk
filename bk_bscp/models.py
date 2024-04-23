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
from dataclasses import dataclass
from typing import Any, Dict, List

from bk_bscp.utils import dict_to_dataclass


@dataclass
class WatchAppInputParams:
    """The input params for sending watch requests."""

    app: str
    uid: str
    labels: Dict[str, str]

    # Optional fields
    appID: int = 0  # NOCC:invalid-name(ignore)
    namespace: str = ""  # NOCC:invalid-name(ignore)
    currentReleaseID: int = 0  # NOCC:invalid-name(ignore)
    currentCursorID: int = 0  # NOCC:invalid-name(ignore)


@dataclass
class KeyRevisionInfo:
    """A key revision info object, used in KeyValueUpdatedEvent."""

    id: int
    key: str
    kv_type: str
    kv_attachment: Dict
    revision: Dict
    content_spec: Dict[str, Any]


@dataclass
class KeyValueUpdatedEvent:
    """An event object that describes changing of key-value pairs."""

    app: str
    app_id: int
    release_id: int
    key_infos: List[KeyRevisionInfo]

    @classmethod
    def from_release_meta(cls, payload: Dict):
        """Create a KeyValueUpdatedEvent from release meta data."""
        return cls(
            app=payload["app"],
            app_id=payload["appID"],
            release_id=payload["releaseID"],
            key_infos=[dict_to_dataclass(d, KeyRevisionInfo) for d in payload["kvMetas"]],
        )


@dataclass
class KeyValuePair:
    """A key-value pair object returned by the bscp server."""

    key: str
    type: str
    value: Any
