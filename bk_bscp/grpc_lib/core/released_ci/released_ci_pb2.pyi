from bk_bscp.grpc_lib.core.base import base_pb2 as _base_pb2
from bk_bscp.grpc_lib.core.commit import commit_pb2 as _commit_pb2
from bk_bscp.grpc_lib.core.config_item import config_item_pb2 as _config_item_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReleasedConfigItem(_message.Message):
    __slots__ = ("id", "release_id", "commit_id", "commit_spec", "config_item_id", "spec", "attachment", "revision")
    ID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    COMMIT_ID_FIELD_NUMBER: _ClassVar[int]
    COMMIT_SPEC_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    id: int
    release_id: int
    commit_id: int
    commit_spec: _commit_pb2.ReleasedCommitSpec
    config_item_id: int
    spec: _config_item_pb2.ConfigItemSpec
    attachment: _config_item_pb2.ConfigItemAttachment
    revision: _base_pb2.Revision
    def __init__(self, id: _Optional[int] = ..., release_id: _Optional[int] = ..., commit_id: _Optional[int] = ..., commit_spec: _Optional[_Union[_commit_pb2.ReleasedCommitSpec, _Mapping]] = ..., config_item_id: _Optional[int] = ..., spec: _Optional[_Union[_config_item_pb2.ConfigItemSpec, _Mapping]] = ..., attachment: _Optional[_Union[_config_item_pb2.ConfigItemAttachment, _Mapping]] = ..., revision: _Optional[_Union[_base_pb2.Revision, _Mapping]] = ...) -> None: ...
