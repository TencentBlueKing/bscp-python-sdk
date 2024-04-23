from bk_bscp.grpc_lib.core.base import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AppTemplateBinding(_message.Message):
    __slots__ = ("id", "spec", "attachment", "revision")
    ID_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    id: int
    spec: AppTemplateBindingSpec
    attachment: AppTemplateBindingAttachment
    revision: _base_pb2.Revision
    def __init__(self, id: _Optional[int] = ..., spec: _Optional[_Union[AppTemplateBindingSpec, _Mapping]] = ..., attachment: _Optional[_Union[AppTemplateBindingAttachment, _Mapping]] = ..., revision: _Optional[_Union[_base_pb2.Revision, _Mapping]] = ...) -> None: ...

class AppTemplateBindingSpec(_message.Message):
    __slots__ = ("template_space_ids", "template_set_ids", "template_ids", "template_revision_ids", "latest_template_ids", "bindings")
    TEMPLATE_SPACE_IDS_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_SET_IDS_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_IDS_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_REVISION_IDS_FIELD_NUMBER: _ClassVar[int]
    LATEST_TEMPLATE_IDS_FIELD_NUMBER: _ClassVar[int]
    BINDINGS_FIELD_NUMBER: _ClassVar[int]
    template_space_ids: _containers.RepeatedScalarFieldContainer[int]
    template_set_ids: _containers.RepeatedScalarFieldContainer[int]
    template_ids: _containers.RepeatedScalarFieldContainer[int]
    template_revision_ids: _containers.RepeatedScalarFieldContainer[int]
    latest_template_ids: _containers.RepeatedScalarFieldContainer[int]
    bindings: _containers.RepeatedCompositeFieldContainer[TemplateBinding]
    def __init__(self, template_space_ids: _Optional[_Iterable[int]] = ..., template_set_ids: _Optional[_Iterable[int]] = ..., template_ids: _Optional[_Iterable[int]] = ..., template_revision_ids: _Optional[_Iterable[int]] = ..., latest_template_ids: _Optional[_Iterable[int]] = ..., bindings: _Optional[_Iterable[_Union[TemplateBinding, _Mapping]]] = ...) -> None: ...

class TemplateBinding(_message.Message):
    __slots__ = ("template_set_id", "template_revisions")
    TEMPLATE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_REVISIONS_FIELD_NUMBER: _ClassVar[int]
    template_set_id: int
    template_revisions: _containers.RepeatedCompositeFieldContainer[TemplateRevisionBinding]
    def __init__(self, template_set_id: _Optional[int] = ..., template_revisions: _Optional[_Iterable[_Union[TemplateRevisionBinding, _Mapping]]] = ...) -> None: ...

class TemplateRevisionBinding(_message.Message):
    __slots__ = ("template_id", "template_revision_id", "is_latest")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_LATEST_FIELD_NUMBER: _ClassVar[int]
    template_id: int
    template_revision_id: int
    is_latest: bool
    def __init__(self, template_id: _Optional[int] = ..., template_revision_id: _Optional[int] = ..., is_latest: bool = ...) -> None: ...

class AppTemplateBindingAttachment(_message.Message):
    __slots__ = ("biz_id", "app_id")
    BIZ_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    biz_id: int
    app_id: int
    def __init__(self, biz_id: _Optional[int] = ..., app_id: _Optional[int] = ...) -> None: ...

class AppBoundTmplRevisionGroupBySet(_message.Message):
    __slots__ = ("template_space_id", "template_space_name", "template_set_id", "template_set_name", "template_revisions")
    class template_revision_detail(_message.Message):
        __slots__ = ("template_id", "name", "path", "template_revision_id", "is_latest", "template_revision_name", "template_revision_memo", "file_type", "file_mode", "user", "user_group", "privilege", "signature", "byte_size", "creator", "create_at", "file_state", "md5")
        TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
        IS_LATEST_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_REVISION_NAME_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_REVISION_MEMO_FIELD_NUMBER: _ClassVar[int]
        FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
        FILE_MODE_FIELD_NUMBER: _ClassVar[int]
        USER_FIELD_NUMBER: _ClassVar[int]
        USER_GROUP_FIELD_NUMBER: _ClassVar[int]
        PRIVILEGE_FIELD_NUMBER: _ClassVar[int]
        SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        BYTE_SIZE_FIELD_NUMBER: _ClassVar[int]
        CREATOR_FIELD_NUMBER: _ClassVar[int]
        CREATE_AT_FIELD_NUMBER: _ClassVar[int]
        FILE_STATE_FIELD_NUMBER: _ClassVar[int]
        MD5_FIELD_NUMBER: _ClassVar[int]
        template_id: int
        name: str
        path: str
        template_revision_id: int
        is_latest: bool
        template_revision_name: str
        template_revision_memo: str
        file_type: str
        file_mode: str
        user: str
        user_group: str
        privilege: str
        signature: str
        byte_size: int
        creator: str
        create_at: str
        file_state: str
        md5: str
        def __init__(self, template_id: _Optional[int] = ..., name: _Optional[str] = ..., path: _Optional[str] = ..., template_revision_id: _Optional[int] = ..., is_latest: bool = ..., template_revision_name: _Optional[str] = ..., template_revision_memo: _Optional[str] = ..., file_type: _Optional[str] = ..., file_mode: _Optional[str] = ..., user: _Optional[str] = ..., user_group: _Optional[str] = ..., privilege: _Optional[str] = ..., signature: _Optional[str] = ..., byte_size: _Optional[int] = ..., creator: _Optional[str] = ..., create_at: _Optional[str] = ..., file_state: _Optional[str] = ..., md5: _Optional[str] = ...) -> None: ...
    TEMPLATE_SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_SPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_SET_NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_REVISIONS_FIELD_NUMBER: _ClassVar[int]
    template_space_id: int
    template_space_name: str
    template_set_id: int
    template_set_name: str
    template_revisions: _containers.RepeatedCompositeFieldContainer[AppBoundTmplRevisionGroupBySet.template_revision_detail]
    def __init__(self, template_space_id: _Optional[int] = ..., template_space_name: _Optional[str] = ..., template_set_id: _Optional[int] = ..., template_set_name: _Optional[str] = ..., template_revisions: _Optional[_Iterable[_Union[AppBoundTmplRevisionGroupBySet.template_revision_detail, _Mapping]]] = ...) -> None: ...

class ReleasedAppBoundTmplRevisionGroupBySet(_message.Message):
    __slots__ = ("template_space_id", "template_space_name", "template_set_id", "template_set_name", "template_revisions")
    class template_revision_detail(_message.Message):
        __slots__ = ("template_id", "name", "path", "template_revision_id", "is_latest", "template_revision_name", "template_revision_memo", "file_type", "file_mode", "user", "user_group", "privilege", "signature", "byte_size", "origin_signature", "origin_byte_size", "creator", "reviser", "create_at", "update_at", "md5")
        TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
        IS_LATEST_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_REVISION_NAME_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_REVISION_MEMO_FIELD_NUMBER: _ClassVar[int]
        FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
        FILE_MODE_FIELD_NUMBER: _ClassVar[int]
        USER_FIELD_NUMBER: _ClassVar[int]
        USER_GROUP_FIELD_NUMBER: _ClassVar[int]
        PRIVILEGE_FIELD_NUMBER: _ClassVar[int]
        SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        BYTE_SIZE_FIELD_NUMBER: _ClassVar[int]
        ORIGIN_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        ORIGIN_BYTE_SIZE_FIELD_NUMBER: _ClassVar[int]
        CREATOR_FIELD_NUMBER: _ClassVar[int]
        REVISER_FIELD_NUMBER: _ClassVar[int]
        CREATE_AT_FIELD_NUMBER: _ClassVar[int]
        UPDATE_AT_FIELD_NUMBER: _ClassVar[int]
        MD5_FIELD_NUMBER: _ClassVar[int]
        template_id: int
        name: str
        path: str
        template_revision_id: int
        is_latest: bool
        template_revision_name: str
        template_revision_memo: str
        file_type: str
        file_mode: str
        user: str
        user_group: str
        privilege: str
        signature: str
        byte_size: int
        origin_signature: str
        origin_byte_size: int
        creator: str
        reviser: str
        create_at: str
        update_at: str
        md5: str
        def __init__(self, template_id: _Optional[int] = ..., name: _Optional[str] = ..., path: _Optional[str] = ..., template_revision_id: _Optional[int] = ..., is_latest: bool = ..., template_revision_name: _Optional[str] = ..., template_revision_memo: _Optional[str] = ..., file_type: _Optional[str] = ..., file_mode: _Optional[str] = ..., user: _Optional[str] = ..., user_group: _Optional[str] = ..., privilege: _Optional[str] = ..., signature: _Optional[str] = ..., byte_size: _Optional[int] = ..., origin_signature: _Optional[str] = ..., origin_byte_size: _Optional[int] = ..., creator: _Optional[str] = ..., reviser: _Optional[str] = ..., create_at: _Optional[str] = ..., update_at: _Optional[str] = ..., md5: _Optional[str] = ...) -> None: ...
    TEMPLATE_SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_SPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_SET_NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_REVISIONS_FIELD_NUMBER: _ClassVar[int]
    template_space_id: int
    template_space_name: str
    template_set_id: int
    template_set_name: str
    template_revisions: _containers.RepeatedCompositeFieldContainer[ReleasedAppBoundTmplRevisionGroupBySet.template_revision_detail]
    def __init__(self, template_space_id: _Optional[int] = ..., template_space_name: _Optional[str] = ..., template_set_id: _Optional[int] = ..., template_set_name: _Optional[str] = ..., template_revisions: _Optional[_Iterable[_Union[ReleasedAppBoundTmplRevisionGroupBySet.template_revision_detail, _Mapping]]] = ...) -> None: ...

class AppBoundTmplRevision(_message.Message):
    __slots__ = ("template_space_id", "template_space_name", "template_set_id", "template_set_name", "template_id", "name", "path", "template_revision_id", "is_latest", "template_revision_name", "template_revision_memo", "file_type", "file_mode", "user", "user_group", "privilege", "signature", "byte_size", "creator", "create_at", "file_state", "md5")
    TEMPLATE_SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_SPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_SET_NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_LATEST_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_REVISION_NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_REVISION_MEMO_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_MODE_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    USER_GROUP_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    BYTE_SIZE_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    CREATE_AT_FIELD_NUMBER: _ClassVar[int]
    FILE_STATE_FIELD_NUMBER: _ClassVar[int]
    MD5_FIELD_NUMBER: _ClassVar[int]
    template_space_id: int
    template_space_name: str
    template_set_id: int
    template_set_name: str
    template_id: int
    name: str
    path: str
    template_revision_id: int
    is_latest: bool
    template_revision_name: str
    template_revision_memo: str
    file_type: str
    file_mode: str
    user: str
    user_group: str
    privilege: str
    signature: str
    byte_size: int
    creator: str
    create_at: str
    file_state: str
    md5: str
    def __init__(self, template_space_id: _Optional[int] = ..., template_space_name: _Optional[str] = ..., template_set_id: _Optional[int] = ..., template_set_name: _Optional[str] = ..., template_id: _Optional[int] = ..., name: _Optional[str] = ..., path: _Optional[str] = ..., template_revision_id: _Optional[int] = ..., is_latest: bool = ..., template_revision_name: _Optional[str] = ..., template_revision_memo: _Optional[str] = ..., file_type: _Optional[str] = ..., file_mode: _Optional[str] = ..., user: _Optional[str] = ..., user_group: _Optional[str] = ..., privilege: _Optional[str] = ..., signature: _Optional[str] = ..., byte_size: _Optional[int] = ..., creator: _Optional[str] = ..., create_at: _Optional[str] = ..., file_state: _Optional[str] = ..., md5: _Optional[str] = ...) -> None: ...

class ReleasedAppBoundTmplRevision(_message.Message):
    __slots__ = ("template_space_id", "template_space_name", "template_set_id", "template_set_name", "template_id", "name", "path", "template_revision_id", "is_latest", "template_revision_name", "template_revision_memo", "file_type", "file_mode", "user", "user_group", "privilege", "signature", "byte_size", "origin_signature", "origin_byte_size", "creator", "reviser", "create_at", "update_at", "md5")
    TEMPLATE_SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_SPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_SET_NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_LATEST_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_REVISION_NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_REVISION_MEMO_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_MODE_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    USER_GROUP_FIELD_NUMBER: _ClassVar[int]
    PRIVILEGE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    BYTE_SIZE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_BYTE_SIZE_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    REVISER_FIELD_NUMBER: _ClassVar[int]
    CREATE_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_AT_FIELD_NUMBER: _ClassVar[int]
    MD5_FIELD_NUMBER: _ClassVar[int]
    template_space_id: int
    template_space_name: str
    template_set_id: int
    template_set_name: str
    template_id: int
    name: str
    path: str
    template_revision_id: int
    is_latest: bool
    template_revision_name: str
    template_revision_memo: str
    file_type: str
    file_mode: str
    user: str
    user_group: str
    privilege: str
    signature: str
    byte_size: int
    origin_signature: str
    origin_byte_size: int
    creator: str
    reviser: str
    create_at: str
    update_at: str
    md5: str
    def __init__(self, template_space_id: _Optional[int] = ..., template_space_name: _Optional[str] = ..., template_set_id: _Optional[int] = ..., template_set_name: _Optional[str] = ..., template_id: _Optional[int] = ..., name: _Optional[str] = ..., path: _Optional[str] = ..., template_revision_id: _Optional[int] = ..., is_latest: bool = ..., template_revision_name: _Optional[str] = ..., template_revision_memo: _Optional[str] = ..., file_type: _Optional[str] = ..., file_mode: _Optional[str] = ..., user: _Optional[str] = ..., user_group: _Optional[str] = ..., privilege: _Optional[str] = ..., signature: _Optional[str] = ..., byte_size: _Optional[int] = ..., origin_signature: _Optional[str] = ..., origin_byte_size: _Optional[int] = ..., creator: _Optional[str] = ..., reviser: _Optional[str] = ..., create_at: _Optional[str] = ..., update_at: _Optional[str] = ..., md5: _Optional[str] = ...) -> None: ...

class Conflict(_message.Message):
    __slots__ = ("template_set_id", "template_set_name", "template_id", "template_name")
    TEMPLATE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_SET_NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    template_set_id: int
    template_set_name: str
    template_id: int
    template_name: str
    def __init__(self, template_set_id: _Optional[int] = ..., template_set_name: _Optional[str] = ..., template_id: _Optional[int] = ..., template_name: _Optional[str] = ...) -> None: ...
