from bk_bscp.grpc_lib.core.base import base_pb2 as _base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class App(_message.Message):
    __slots__ = ("id", "biz_id", "space_id", "space_type_id", "space_name", "space_type_name", "spec", "revision")
    ID_FIELD_NUMBER: _ClassVar[int]
    BIZ_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    SPACE_TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    id: int
    biz_id: int
    space_id: str
    space_type_id: str
    space_name: str
    space_type_name: str
    spec: AppSpec
    revision: _base_pb2.Revision
    def __init__(self, id: _Optional[int] = ..., biz_id: _Optional[int] = ..., space_id: _Optional[str] = ..., space_type_id: _Optional[str] = ..., space_name: _Optional[str] = ..., space_type_name: _Optional[str] = ..., spec: _Optional[_Union[AppSpec, _Mapping]] = ..., revision: _Optional[_Union[_base_pb2.Revision, _Mapping]] = ...) -> None: ...

class AppSpec(_message.Message):
    __slots__ = ("name", "config_type", "memo", "alias", "data_type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_TYPE_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    config_type: str
    memo: str
    alias: str
    data_type: str
    def __init__(self, name: _Optional[str] = ..., config_type: _Optional[str] = ..., memo: _Optional[str] = ..., alias: _Optional[str] = ..., data_type: _Optional[str] = ...) -> None: ...
