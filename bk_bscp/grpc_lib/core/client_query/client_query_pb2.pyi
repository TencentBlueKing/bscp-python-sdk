from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClientQuery(_message.Message):
    __slots__ = ("id", "spec", "attachment")
    ID_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    id: int
    spec: ClientQuerySpec
    attachment: ClientQueryAttachment
    def __init__(self, id: _Optional[int] = ..., spec: _Optional[_Union[ClientQuerySpec, _Mapping]] = ..., attachment: _Optional[_Union[ClientQueryAttachment, _Mapping]] = ...) -> None: ...

class ClientQuerySpec(_message.Message):
    __slots__ = ("creator", "search_type", "search_name", "search_condition", "created_at", "updated_at")
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    SEARCH_TYPE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_NAME_FIELD_NUMBER: _ClassVar[int]
    SEARCH_CONDITION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    creator: str
    search_type: str
    search_name: str
    search_condition: _struct_pb2.Struct
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, creator: _Optional[str] = ..., search_type: _Optional[str] = ..., search_name: _Optional[str] = ..., search_condition: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ClientQueryAttachment(_message.Message):
    __slots__ = ("biz_id", "app_id")
    BIZ_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    biz_id: int
    app_id: int
    def __init__(self, biz_id: _Optional[int] = ..., app_id: _Optional[int] = ...) -> None: ...
