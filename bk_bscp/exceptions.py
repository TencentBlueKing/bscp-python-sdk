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
"""Exceptions for bk_bscp."""


class BscpClientBaseError(Exception):
    """The base class for all BSCP client errors."""


class BscpClientConnectionError(BscpClientBaseError):
    """Raised when there is an error connecting to the BSCP server."""


class BscpClientRequestError(BscpClientBaseError):
    """The base class for all BSCP client request errors."""

    def __init__(self, message: str, exc: Exception):
        self.orig_exception = exc
        super().__init__(message)


class BscpClientHandshakeError(BscpClientRequestError):
    """Raised when there is an error handshaking with the BSCP server."""


class BscpClientGetError(BscpClientRequestError):
    """Raised when there is an error getting key-value pairs."""


class BscpClientWatchError(BscpClientBaseError):
    """Raised when there is an error watching changes."""

    def __init__(self, code: str, details: str, exc: Exception):
        self.orig_exception = exc
        super().__init__(f"{code}: {details}")


class BscpClientWatchBounceError(BscpClientBaseError):
    """Raised when a server bounce is detected."""
