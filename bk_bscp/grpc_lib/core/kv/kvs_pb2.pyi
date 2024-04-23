from bk_bscp.grpc_lib.core.base import base_pb2 as _base_pb2
from bk_bscp.grpc_lib.core.content import content_pb2 as _content_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Kv(_message.Message):
    __slots__ = ("id", "kv_state", "spec", "attachment", "revision", "content_spec")
    ID_FIELD_NUMBER: _ClassVar[int]
    KV_STATE_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    CONTENT_SPEC_FIELD_NUMBER: _ClassVar[int]
    id: int
    kv_state: str
    spec: KvSpec
    attachment: KvAttachment
    revision: _base_pb2.Revision
    content_spec: _content_pb2.ContentSpec
    def __init__(self, id: _Optional[int] = ..., kv_state: _Optional[str] = ..., spec: _Optional[_Union[KvSpec, _Mapping]] = ..., attachment: _Optional[_Union[KvAttachment, _Mapping]] = ..., revision: _Optional[_Union[_base_pb2.Revision, _Mapping]] = ..., content_spec: _Optional[_Union[_content_pb2.ContentSpec, _Mapping]] = ...) -> None: ...

class KvSpec(_message.Message):
    __slots__ = ("key", "kv_type", "value", "memo")
    KEY_FIELD_NUMBER: _ClassVar[int]
    KV_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    key: str
    kv_type: str
    value: str
    memo: str
    def __init__(self, key: _Optional[str] = ..., kv_type: _Optional[str] = ..., value: _Optional[str] = ..., memo: _Optional[str] = ...) -> None: ...

class KvAttachment(_message.Message):
    __slots__ = ("biz_id", "app_id")
    BIZ_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    biz_id: int
    app_id: int
    def __init__(self, biz_id: _Optional[int] = ..., app_id: _Optional[int] = ...) -> None: ...
