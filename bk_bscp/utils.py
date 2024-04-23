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
"""Utilities"""
import dataclasses
import uuid
from typing import Any, Dict, Type, TypeVar


def get_fingerprint() -> str:
    """Get the fingerprint for communication with the feed server."""
    # TODO: Update the algo for generating fingerprint.
    return uuid.uuid4().hex


T = TypeVar("T")


def dict_to_dataclass(data: Dict[str, Any], cls: Type[T]) -> T:
    """Convert a dict to a dataclass object, this function is safer than `cls(**obj)`
    because it ignores unrelated fields in the dict before the conversion.

    :param data: The dict object.
    :param cls: The dataclass type.
    :raises TypeError: When the cls is not a dataclass.
    """
    if not dataclasses.is_dataclass(cls):
        raise TypeError("not a dataclass")

    valid_fields = [f.name for f in dataclasses.fields(cls)]
    kwargs = {k: v for k, v in data.items() if k in valid_fields}
    return cls(**kwargs)  # type: ignore
