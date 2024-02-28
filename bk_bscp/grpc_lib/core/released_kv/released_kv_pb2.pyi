from bk_bscp.grpc_lib.core.base import base_pb2 as _base_pb2
from bk_bscp.grpc_lib.core.kv import kvs_pb2 as _kvs_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReleasedKv(_message.Message):
    __slots__ = ("id", "release_id", "spec", "attachment", "revision")
    ID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    id: int
    release_id: int
    spec: _kvs_pb2.KvSpec
    attachment: _kvs_pb2.KvAttachment
    revision: _base_pb2.Revision
    def __init__(self, id: _Optional[int] = ..., release_id: _Optional[int] = ..., spec: _Optional[_Union[_kvs_pb2.KvSpec, _Mapping]] = ..., attachment: _Optional[_Union[_kvs_pb2.KvAttachment, _Mapping]] = ..., revision: _Optional[_Union[_base_pb2.Revision, _Mapping]] = ...) -> None: ...
