from bk_bscp.grpc_lib.core.base import base_pb2 as _base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TemplateVariable(_message.Message):
    __slots__ = ("id", "spec", "attachment", "revision")
    ID_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    id: int
    spec: TemplateVariableSpec
    attachment: TemplateVariableAttachment
    revision: _base_pb2.Revision
    def __init__(self, id: _Optional[int] = ..., spec: _Optional[_Union[TemplateVariableSpec, _Mapping]] = ..., attachment: _Optional[_Union[TemplateVariableAttachment, _Mapping]] = ..., revision: _Optional[_Union[_base_pb2.Revision, _Mapping]] = ...) -> None: ...

class TemplateVariableSpec(_message.Message):
    __slots__ = ("name", "type", "default_val", "memo")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VAL_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    default_val: str
    memo: str
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., default_val: _Optional[str] = ..., memo: _Optional[str] = ...) -> None: ...

class TemplateVariableAttachment(_message.Message):
    __slots__ = ("biz_id",)
    BIZ_ID_FIELD_NUMBER: _ClassVar[int]
    biz_id: int
    def __init__(self, biz_id: _Optional[int] = ...) -> None: ...
