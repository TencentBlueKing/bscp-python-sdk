from bk_bscp.grpc_lib.core.base import base_pb2 as _base_pb2
from bk_bscp.grpc_lib.core.commit import commit_pb2 as _commit_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigItem(_message.Message):
    __slots__ = ("id", "config_item_id", "file_state", "spec", "commit_spec", "attachment", "revision")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_STATE_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    COMMIT_SPEC_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    id: int
    config_item_id: int
    file_state: str
    spec: ConfigItemSpec
    commit_spec: _commit_pb2.CommitSpec
    attachment: ConfigItemAttachment
    revision: _base_pb2.Revision
    def __init__(self, id: _Optional[int] = ..., config_item_id: _Optional[int] = ..., file_state: _Optional[str] = ..., spec: _Optional[_Union[ConfigItemSpec, _Mapping]] = ..., commit_spec: _Optional[_Union[_commit_pb2.CommitSpec, _Mapping]] = ..., attachment: _Optional[_Union[ConfigItemAttachment, _Mapping]] = ..., revision: _Optional[_Union[_base_pb2.Revision, _Mapping]] = ...) -> None: ...

class ConfigItemSpec(_message.Message):
    __slots__ = ("name", "path", "file_type", "file_mode", "memo", "permission")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_MODE_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    path: str
    file_type: str
    file_mode: str
    memo: str
    permission: FilePermission
    def __init__(self, name: _Optional[str] = ..., path: _Optional[str] = ..., file_type: _Optional[str] = ..., file_mode: _Optional[str] = ..., memo: _Optional[str] = ..., permission: _Optional[_Union[FilePermission, _Mapping]] = ...) -> None: ...

class ConfigItemAttachment(_message.Message):
    __slots__ = ("biz_id", "app_id")
    BIZ_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    biz_id: int
    app_id: int
    def __init__(self, biz_id: _Optional[int] = ..., app_id: _Optional[int] = ...) -> None: ...

class FilePermission(_message.Message):
    __slots__ = ("user", "user_group", "privilege")
    USER_FIELD_NUMBER: _ClassVar[int]
    USER_GROUP_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGE_FIELD_NUMBER: _ClassVar[int]
    user: str
    user_group: str
    privilege: str
    def __init__(self, user: _Optional[str] = ..., user_group: _Optional[str] = ..., privilege: _Optional[str] = ...) -> None: ...

class ListConfigItemCounts(_message.Message):
    __slots__ = ("app_id", "count", "update_at")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_AT_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    count: int
    update_at: str
    def __init__(self, app_id: _Optional[int] = ..., count: _Optional[int] = ..., update_at: _Optional[str] = ...) -> None: ...
