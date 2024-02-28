from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EventSpec(_message.Message):
    __slots__ = ("resource", "resource_id", "resource_uid", "op_type")
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_UID_FIELD_NUMBER: _ClassVar[int]
    OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    resource: str
    resource_id: int
    resource_uid: str
    op_type: str
    def __init__(self, resource: _Optional[str] = ..., resource_id: _Optional[int] = ..., resource_uid: _Optional[str] = ..., op_type: _Optional[str] = ...) -> None: ...

class EventAttachment(_message.Message):
    __slots__ = ("biz_id", "app_id")
    BIZ_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    biz_id: int
    app_id: int
    def __init__(self, biz_id: _Optional[int] = ..., app_id: _Optional[int] = ...) -> None: ...
