from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReleasedGroup(_message.Message):
    __slots__ = ("id", "group_id", "app_id", "release_id", "strategy_id", "edited", "biz_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_ID_FIELD_NUMBER: _ClassVar[int]
    EDITED_FIELD_NUMBER: _ClassVar[int]
    BIZ_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    group_id: int
    app_id: int
    release_id: int
    strategy_id: int
    edited: bool
    biz_id: int
    def __init__(self, id: _Optional[int] = ..., group_id: _Optional[int] = ..., app_id: _Optional[int] = ..., release_id: _Optional[int] = ..., strategy_id: _Optional[int] = ..., edited: bool = ..., biz_id: _Optional[int] = ...) -> None: ...
