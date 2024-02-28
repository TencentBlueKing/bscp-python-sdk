from google.protobuf import struct_pb2 as _struct_pb2
from bk_bscp.grpc_lib.core.base import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Group(_message.Message):
    __slots__ = ("id", "spec", "attachment", "revision")
    ID_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    id: int
    spec: GroupSpec
    attachment: GroupAttachment
    revision: _base_pb2.Revision
    def __init__(self, id: _Optional[int] = ..., spec: _Optional[_Union[GroupSpec, _Mapping]] = ..., attachment: _Optional[_Union[GroupAttachment, _Mapping]] = ..., revision: _Optional[_Union[_base_pb2.Revision, _Mapping]] = ...) -> None: ...

class GroupSpec(_message.Message):
    __slots__ = ("name", "public", "bind_apps", "mode", "selector", "uid")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    BIND_APPS_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    SELECTOR_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    name: str
    public: bool
    bind_apps: _containers.RepeatedScalarFieldContainer[int]
    mode: str
    selector: _struct_pb2.Struct
    uid: str
    def __init__(self, name: _Optional[str] = ..., public: bool = ..., bind_apps: _Optional[_Iterable[int]] = ..., mode: _Optional[str] = ..., selector: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., uid: _Optional[str] = ...) -> None: ...

class GroupAttachment(_message.Message):
    __slots__ = ("biz_id",)
    BIZ_ID_FIELD_NUMBER: _ClassVar[int]
    biz_id: int
    def __init__(self, biz_id: _Optional[int] = ...) -> None: ...
