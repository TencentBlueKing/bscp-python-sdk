from google.protobuf import struct_pb2 as _struct_pb2
from bk_bscp.grpc_lib.core.base import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Release(_message.Message):
    __slots__ = ("id", "spec", "status", "attachment", "revision")
    ID_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    id: int
    spec: ReleaseSpec
    status: ReleaseStatus
    attachment: ReleaseAttachment
    revision: _base_pb2.CreatedRevision
    def __init__(self, id: _Optional[int] = ..., spec: _Optional[_Union[ReleaseSpec, _Mapping]] = ..., status: _Optional[_Union[ReleaseStatus, _Mapping]] = ..., attachment: _Optional[_Union[ReleaseAttachment, _Mapping]] = ..., revision: _Optional[_Union[_base_pb2.CreatedRevision, _Mapping]] = ...) -> None: ...

class ReleaseSpec(_message.Message):
    __slots__ = ("name", "memo", "deprecated", "publish_num")
    NAME_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_NUM_FIELD_NUMBER: _ClassVar[int]
    name: str
    memo: str
    deprecated: bool
    publish_num: int
    def __init__(self, name: _Optional[str] = ..., memo: _Optional[str] = ..., deprecated: bool = ..., publish_num: _Optional[int] = ...) -> None: ...

class ReleaseStatus(_message.Message):
    __slots__ = ("publish_status", "released_groups", "fully_released")
    class ReleasedGroup(_message.Message):
        __slots__ = ("id", "name", "mode", "old_selector", "new_selector", "uid", "edited")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        MODE_FIELD_NUMBER: _ClassVar[int]
        OLD_SELECTOR_FIELD_NUMBER: _ClassVar[int]
        NEW_SELECTOR_FIELD_NUMBER: _ClassVar[int]
        UID_FIELD_NUMBER: _ClassVar[int]
        EDITED_FIELD_NUMBER: _ClassVar[int]
        id: int
        name: str
        mode: str
        old_selector: _struct_pb2.Struct
        new_selector: _struct_pb2.Struct
        uid: str
        edited: bool
        def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., mode: _Optional[str] = ..., old_selector: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., new_selector: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., uid: _Optional[str] = ..., edited: bool = ...) -> None: ...
    PUBLISH_STATUS_FIELD_NUMBER: _ClassVar[int]
    RELEASED_GROUPS_FIELD_NUMBER: _ClassVar[int]
    FULLY_RELEASED_FIELD_NUMBER: _ClassVar[int]
    publish_status: str
    released_groups: _containers.RepeatedCompositeFieldContainer[ReleaseStatus.ReleasedGroup]
    fully_released: bool
    def __init__(self, publish_status: _Optional[str] = ..., released_groups: _Optional[_Iterable[_Union[ReleaseStatus.ReleasedGroup, _Mapping]]] = ..., fully_released: bool = ...) -> None: ...

class ReleaseAttachment(_message.Message):
    __slots__ = ("biz_id", "app_id")
    BIZ_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    biz_id: int
    app_id: int
    def __init__(self, biz_id: _Optional[int] = ..., app_id: _Optional[int] = ...) -> None: ...
