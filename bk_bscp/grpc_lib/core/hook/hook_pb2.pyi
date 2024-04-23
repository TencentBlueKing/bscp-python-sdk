from bk_bscp.grpc_lib.core.base import base_pb2 as _base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Hook(_message.Message):
    __slots__ = ("id", "spec", "attachment", "revision")
    ID_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    id: int
    spec: HookSpec
    attachment: HookAttachment
    revision: _base_pb2.Revision
    def __init__(self, id: _Optional[int] = ..., spec: _Optional[_Union[HookSpec, _Mapping]] = ..., attachment: _Optional[_Union[HookAttachment, _Mapping]] = ..., revision: _Optional[_Union[_base_pb2.Revision, _Mapping]] = ...) -> None: ...

class HookSpec(_message.Message):
    __slots__ = ("name", "type", "tag", "memo", "content", "revision_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    REVISION_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    tag: str
    memo: str
    content: str
    revision_name: str
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., tag: _Optional[str] = ..., memo: _Optional[str] = ..., content: _Optional[str] = ..., revision_name: _Optional[str] = ...) -> None: ...

class HookAttachment(_message.Message):
    __slots__ = ("biz_id",)
    BIZ_ID_FIELD_NUMBER: _ClassVar[int]
    biz_id: int
    def __init__(self, biz_id: _Optional[int] = ...) -> None: ...

class ListHookTagCounts(_message.Message):
    __slots__ = ("app_id", "tag", "count", "update_at")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_AT_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    tag: str
    count: int
    update_at: str
    def __init__(self, app_id: _Optional[int] = ..., tag: _Optional[str] = ..., count: _Optional[int] = ..., update_at: _Optional[str] = ...) -> None: ...

class CountHookTags(_message.Message):
    __slots__ = ("tag", "counts")
    TAG_FIELD_NUMBER: _ClassVar[int]
    COUNTS_FIELD_NUMBER: _ClassVar[int]
    tag: str
    counts: int
    def __init__(self, tag: _Optional[str] = ..., counts: _Optional[int] = ...) -> None: ...
