from bk_bscp.grpc_lib.core.base import base_pb2 as _base_pb2
from bk_bscp.grpc_lib.core.content import content_pb2 as _content_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Commit(_message.Message):
    __slots__ = ("id", "spec", "attachment", "revision")
    ID_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    id: int
    spec: CommitSpec
    attachment: CommitAttachment
    revision: _base_pb2.CreatedRevision
    def __init__(self, id: _Optional[int] = ..., spec: _Optional[_Union[CommitSpec, _Mapping]] = ..., attachment: _Optional[_Union[CommitAttachment, _Mapping]] = ..., revision: _Optional[_Union[_base_pb2.CreatedRevision, _Mapping]] = ...) -> None: ...

class CommitSpec(_message.Message):
    __slots__ = ("content_id", "content", "memo")
    CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    content_id: int
    content: _content_pb2.ContentSpec
    memo: str
    def __init__(self, content_id: _Optional[int] = ..., content: _Optional[_Union[_content_pb2.ContentSpec, _Mapping]] = ..., memo: _Optional[str] = ...) -> None: ...

class ReleasedCommitSpec(_message.Message):
    __slots__ = ("content_id", "content", "memo")
    CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    content_id: int
    content: _content_pb2.ReleasedContentSpec
    memo: str
    def __init__(self, content_id: _Optional[int] = ..., content: _Optional[_Union[_content_pb2.ReleasedContentSpec, _Mapping]] = ..., memo: _Optional[str] = ...) -> None: ...

class CommitAttachment(_message.Message):
    __slots__ = ("biz_id", "app_id", "config_item_id")
    BIZ_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    biz_id: int
    app_id: int
    config_item_id: int
    def __init__(self, biz_id: _Optional[int] = ..., app_id: _Optional[int] = ..., config_item_id: _Optional[int] = ...) -> None: ...
