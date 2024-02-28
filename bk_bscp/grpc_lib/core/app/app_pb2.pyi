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
    __slots__ = ("name", "config_type", "mode", "memo", "reload", "alias", "data_type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_TYPE_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    RELOAD_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    config_type: str
    mode: str
    memo: str
    reload: Reload
    alias: str
    data_type: str
    def __init__(self, name: _Optional[str] = ..., config_type: _Optional[str] = ..., mode: _Optional[str] = ..., memo: _Optional[str] = ..., reload: _Optional[_Union[Reload, _Mapping]] = ..., alias: _Optional[str] = ..., data_type: _Optional[str] = ...) -> None: ...

class Reload(_message.Message):
    __slots__ = ("reload_type", "file_reload_spec")
    RELOAD_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_RELOAD_SPEC_FIELD_NUMBER: _ClassVar[int]
    reload_type: str
    file_reload_spec: FileReloadSpec
    def __init__(self, reload_type: _Optional[str] = ..., file_reload_spec: _Optional[_Union[FileReloadSpec, _Mapping]] = ...) -> None: ...

class FileReloadSpec(_message.Message):
    __slots__ = ("reload_file_path",)
    RELOAD_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    reload_file_path: str
    def __init__(self, reload_file_path: _Optional[str] = ...) -> None: ...
