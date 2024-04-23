from bk_bscp.grpc_lib.core.base import base_pb2 as _base_pb2
from bk_bscp.grpc_lib.core.commit import commit_pb2 as _commit_pb2
from bk_bscp.grpc_lib.core.config_item import config_item_pb2 as _config_item_pb2
from bk_bscp.grpc_lib.core.hook import hook_pb2 as _hook_pb2
from bk_bscp.grpc_lib.core.kv import kvs_pb2 as _kvs_pb2
from bk_bscp.grpc_lib.core.content import content_pb2 as _content_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SidecarSpec(_message.Message):
    __slots__ = ("biz_id", "version")
    BIZ_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    biz_id: int
    version: _base_pb2.Versioning
    def __init__(self, biz_id: _Optional[int] = ..., version: _Optional[_Union[_base_pb2.Versioning, _Mapping]] = ...) -> None: ...

class HandshakeMessage(_message.Message):
    __slots__ = ("api_version", "spec")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    api_version: _base_pb2.Versioning
    spec: SidecarSpec
    def __init__(self, api_version: _Optional[_Union[_base_pb2.Versioning, _Mapping]] = ..., spec: _Optional[_Union[SidecarSpec, _Mapping]] = ...) -> None: ...

class HandshakeResp(_message.Message):
    __slots__ = ("api_version", "payload")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    api_version: _base_pb2.Versioning
    payload: bytes
    def __init__(self, api_version: _Optional[_Union[_base_pb2.Versioning, _Mapping]] = ..., payload: _Optional[bytes] = ...) -> None: ...

class MessagingMeta(_message.Message):
    __slots__ = ("api_version", "rid", "type", "payload")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    api_version: _base_pb2.Versioning
    rid: str
    type: int
    payload: bytes
    def __init__(self, api_version: _Optional[_Union[_base_pb2.Versioning, _Mapping]] = ..., rid: _Optional[str] = ..., type: _Optional[int] = ..., payload: _Optional[bytes] = ...) -> None: ...

class MessagingResp(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SideWatchMeta(_message.Message):
    __slots__ = ("api_version", "payload")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    api_version: _base_pb2.Versioning
    payload: bytes
    def __init__(self, api_version: _Optional[_Union[_base_pb2.Versioning, _Mapping]] = ..., payload: _Optional[bytes] = ...) -> None: ...

class FeedWatchMessage(_message.Message):
    __slots__ = ("api_version", "rid", "type", "payload")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    api_version: _base_pb2.Versioning
    rid: str
    type: int
    payload: bytes
    def __init__(self, api_version: _Optional[_Union[_base_pb2.Versioning, _Mapping]] = ..., rid: _Optional[str] = ..., type: _Optional[int] = ..., payload: _Optional[bytes] = ...) -> None: ...

class AppMeta(_message.Message):
    __slots__ = ("app", "uid", "labels")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    APP_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    app: str
    uid: str
    labels: _containers.ScalarMap[str, str]
    def __init__(self, app: _Optional[str] = ..., uid: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Repository(_message.Message):
    __slots__ = ("root",)
    ROOT_FIELD_NUMBER: _ClassVar[int]
    root: str
    def __init__(self, root: _Optional[str] = ...) -> None: ...

class RepositorySpec(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class FileMeta(_message.Message):
    __slots__ = ("id", "commit_id", "commit_spec", "config_item_spec", "config_item_attachment", "repository_spec", "config_item_revision")
    ID_FIELD_NUMBER: _ClassVar[int]
    COMMIT_ID_FIELD_NUMBER: _ClassVar[int]
    COMMIT_SPEC_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ITEM_SPEC_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ITEM_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    REPOSITORY_SPEC_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ITEM_REVISION_FIELD_NUMBER: _ClassVar[int]
    id: int
    commit_id: int
    commit_spec: _commit_pb2.CommitSpec
    config_item_spec: _config_item_pb2.ConfigItemSpec
    config_item_attachment: _config_item_pb2.ConfigItemAttachment
    repository_spec: RepositorySpec
    config_item_revision: _base_pb2.Revision
    def __init__(self, id: _Optional[int] = ..., commit_id: _Optional[int] = ..., commit_spec: _Optional[_Union[_commit_pb2.CommitSpec, _Mapping]] = ..., config_item_spec: _Optional[_Union[_config_item_pb2.ConfigItemSpec, _Mapping]] = ..., config_item_attachment: _Optional[_Union[_config_item_pb2.ConfigItemAttachment, _Mapping]] = ..., repository_spec: _Optional[_Union[RepositorySpec, _Mapping]] = ..., config_item_revision: _Optional[_Union[_base_pb2.Revision, _Mapping]] = ...) -> None: ...

class PullAppFileMetaReq(_message.Message):
    __slots__ = ("api_version", "biz_id", "app_meta", "token", "key")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    BIZ_ID_FIELD_NUMBER: _ClassVar[int]
    APP_META_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    api_version: _base_pb2.Versioning
    biz_id: int
    app_meta: AppMeta
    token: str
    key: str
    def __init__(self, api_version: _Optional[_Union[_base_pb2.Versioning, _Mapping]] = ..., biz_id: _Optional[int] = ..., app_meta: _Optional[_Union[AppMeta, _Mapping]] = ..., token: _Optional[str] = ..., key: _Optional[str] = ...) -> None: ...

class PullAppFileMetaResp(_message.Message):
    __slots__ = ("release_id", "release_name", "repository", "file_metas", "pre_hook", "post_hook")
    RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_NAME_FIELD_NUMBER: _ClassVar[int]
    REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    FILE_METAS_FIELD_NUMBER: _ClassVar[int]
    PRE_HOOK_FIELD_NUMBER: _ClassVar[int]
    POST_HOOK_FIELD_NUMBER: _ClassVar[int]
    release_id: int
    release_name: str
    repository: Repository
    file_metas: _containers.RepeatedCompositeFieldContainer[FileMeta]
    pre_hook: _hook_pb2.HookSpec
    post_hook: _hook_pb2.HookSpec
    def __init__(self, release_id: _Optional[int] = ..., release_name: _Optional[str] = ..., repository: _Optional[_Union[Repository, _Mapping]] = ..., file_metas: _Optional[_Iterable[_Union[FileMeta, _Mapping]]] = ..., pre_hook: _Optional[_Union[_hook_pb2.HookSpec, _Mapping]] = ..., post_hook: _Optional[_Union[_hook_pb2.HookSpec, _Mapping]] = ...) -> None: ...

class GetDownloadURLReq(_message.Message):
    __slots__ = ("api_version", "biz_id", "file_meta", "token")
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    BIZ_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_META_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    api_version: _base_pb2.Versioning
    biz_id: int
    file_meta: FileMeta
    token: str
    def __init__(self, api_version: _Optional[_Union[_base_pb2.Versioning, _Mapping]] = ..., biz_id: _Optional[int] = ..., file_meta: _Optional[_Union[FileMeta, _Mapping]] = ..., token: _Optional[str] = ...) -> None: ...

class GetDownloadURLResp(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class App(_message.Message):
    __slots__ = ("id", "name", "config_type", "revision")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_TYPE_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    config_type: str
    revision: _base_pb2.Revision
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., config_type: _Optional[str] = ..., revision: _Optional[_Union[_base_pb2.Revision, _Mapping]] = ...) -> None: ...

class ListAppsReq(_message.Message):
    __slots__ = ("biz_id", "match")
    BIZ_ID_FIELD_NUMBER: _ClassVar[int]
    MATCH_FIELD_NUMBER: _ClassVar[int]
    biz_id: int
    match: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, biz_id: _Optional[int] = ..., match: _Optional[_Iterable[str]] = ...) -> None: ...

class ListAppsResp(_message.Message):
    __slots__ = ("apps",)
    APPS_FIELD_NUMBER: _ClassVar[int]
    apps: _containers.RepeatedCompositeFieldContainer[App]
    def __init__(self, apps: _Optional[_Iterable[_Union[App, _Mapping]]] = ...) -> None: ...

class PullKvMetaReq(_message.Message):
    __slots__ = ("biz_id", "app_meta", "match")
    BIZ_ID_FIELD_NUMBER: _ClassVar[int]
    APP_META_FIELD_NUMBER: _ClassVar[int]
    MATCH_FIELD_NUMBER: _ClassVar[int]
    biz_id: int
    app_meta: AppMeta
    match: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, biz_id: _Optional[int] = ..., app_meta: _Optional[_Union[AppMeta, _Mapping]] = ..., match: _Optional[_Iterable[str]] = ...) -> None: ...

class PullKvMetaResp(_message.Message):
    __slots__ = ("release_id", "kv_metas")
    RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    KV_METAS_FIELD_NUMBER: _ClassVar[int]
    release_id: int
    kv_metas: _containers.RepeatedCompositeFieldContainer[KvMeta]
    def __init__(self, release_id: _Optional[int] = ..., kv_metas: _Optional[_Iterable[_Union[KvMeta, _Mapping]]] = ...) -> None: ...

class KvMeta(_message.Message):
    __slots__ = ("key", "kv_type", "revision", "kv_attachment", "content_spec")
    KEY_FIELD_NUMBER: _ClassVar[int]
    KV_TYPE_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    KV_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_SPEC_FIELD_NUMBER: _ClassVar[int]
    key: str
    kv_type: str
    revision: _base_pb2.Revision
    kv_attachment: _kvs_pb2.KvAttachment
    content_spec: _content_pb2.ContentSpec
    def __init__(self, key: _Optional[str] = ..., kv_type: _Optional[str] = ..., revision: _Optional[_Union[_base_pb2.Revision, _Mapping]] = ..., kv_attachment: _Optional[_Union[_kvs_pb2.KvAttachment, _Mapping]] = ..., content_spec: _Optional[_Union[_content_pb2.ContentSpec, _Mapping]] = ...) -> None: ...

class GetKvValueReq(_message.Message):
    __slots__ = ("biz_id", "app_meta", "key")
    BIZ_ID_FIELD_NUMBER: _ClassVar[int]
    APP_META_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    biz_id: int
    app_meta: AppMeta
    key: str
    def __init__(self, biz_id: _Optional[int] = ..., app_meta: _Optional[_Union[AppMeta, _Mapping]] = ..., key: _Optional[str] = ...) -> None: ...

class GetKvValueResp(_message.Message):
    __slots__ = ("kv_type", "value")
    KV_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    kv_type: str
    value: str
    def __init__(self, kv_type: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
