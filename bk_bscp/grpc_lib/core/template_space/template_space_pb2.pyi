from bk_bscp.grpc_lib.core.base import base_pb2 as _base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TemplateSpace(_message.Message):
    __slots__ = ("id", "spec", "attachment", "revision")
    ID_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    id: int
    spec: TemplateSpaceSpec
    attachment: TemplateSpaceAttachment
    revision: _base_pb2.Revision
    def __init__(self, id: _Optional[int] = ..., spec: _Optional[_Union[TemplateSpaceSpec, _Mapping]] = ..., attachment: _Optional[_Union[TemplateSpaceAttachment, _Mapping]] = ..., revision: _Optional[_Union[_base_pb2.Revision, _Mapping]] = ...) -> None: ...

class TemplateSpaceSpec(_message.Message):
    __slots__ = ("name", "memo")
    NAME_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    name: str
    memo: str
    def __init__(self, name: _Optional[str] = ..., memo: _Optional[str] = ...) -> None: ...

class TemplateSpaceAttachment(_message.Message):
    __slots__ = ("biz_id",)
    BIZ_ID_FIELD_NUMBER: _ClassVar[int]
    biz_id: int
    def __init__(self, biz_id: _Optional[int] = ...) -> None: ...
