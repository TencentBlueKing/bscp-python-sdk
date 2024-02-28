from bk_bscp.grpc_lib.core.base import base_pb2 as _base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Template(_message.Message):
    __slots__ = ("id", "spec", "attachment", "revision")
    ID_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    id: int
    spec: TemplateSpec
    attachment: TemplateAttachment
    revision: _base_pb2.Revision
    def __init__(self, id: _Optional[int] = ..., spec: _Optional[_Union[TemplateSpec, _Mapping]] = ..., attachment: _Optional[_Union[TemplateAttachment, _Mapping]] = ..., revision: _Optional[_Union[_base_pb2.Revision, _Mapping]] = ...) -> None: ...

class TemplateSpec(_message.Message):
    __slots__ = ("name", "path", "memo")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    name: str
    path: str
    memo: str
    def __init__(self, name: _Optional[str] = ..., path: _Optional[str] = ..., memo: _Optional[str] = ...) -> None: ...

class TemplateAttachment(_message.Message):
    __slots__ = ("biz_id", "template_space_id")
    BIZ_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    biz_id: int
    template_space_id: int
    def __init__(self, biz_id: _Optional[int] = ..., template_space_id: _Optional[int] = ...) -> None: ...
