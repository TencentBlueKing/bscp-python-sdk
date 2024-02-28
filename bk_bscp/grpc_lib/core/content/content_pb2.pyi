from bk_bscp.grpc_lib.core.base import base_pb2 as _base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Content(_message.Message):
    __slots__ = ("id", "spec", "attachment", "revision")
    ID_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    id: int
    spec: ContentSpec
    attachment: ContentAttachment
    revision: _base_pb2.CreatedRevision
    def __init__(self, id: _Optional[int] = ..., spec: _Optional[_Union[ContentSpec, _Mapping]] = ..., attachment: _Optional[_Union[ContentAttachment, _Mapping]] = ..., revision: _Optional[_Union[_base_pb2.CreatedRevision, _Mapping]] = ...) -> None: ...

class ContentSpec(_message.Message):
    __slots__ = ("signature", "byte_size")
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    BYTE_SIZE_FIELD_NUMBER: _ClassVar[int]
    signature: str
    byte_size: int
    def __init__(self, signature: _Optional[str] = ..., byte_size: _Optional[int] = ...) -> None: ...

class ReleasedContentSpec(_message.Message):
    __slots__ = ("signature", "byte_size", "origin_signature", "origin_byte_size")
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    BYTE_SIZE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_BYTE_SIZE_FIELD_NUMBER: _ClassVar[int]
    signature: str
    byte_size: int
    origin_signature: str
    origin_byte_size: int
    def __init__(self, signature: _Optional[str] = ..., byte_size: _Optional[int] = ..., origin_signature: _Optional[str] = ..., origin_byte_size: _Optional[int] = ...) -> None: ...

class ContentAttachment(_message.Message):
    __slots__ = ("biz_id", "app_id", "config_item_id")
    BIZ_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    biz_id: int
    app_id: int
    config_item_id: int
    def __init__(self, biz_id: _Optional[int] = ..., app_id: _Optional[int] = ..., config_item_id: _Optional[int] = ...) -> None: ...
