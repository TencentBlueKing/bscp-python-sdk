from bk_bscp.grpc_lib.core.base import base_pb2 as _base_pb2
from bk_bscp.grpc_lib.core.config_item import config_item_pb2 as _config_item_pb2
from bk_bscp.grpc_lib.core.content import content_pb2 as _content_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TemplateRevision(_message.Message):
    __slots__ = ("id", "spec", "attachment", "revision")
    ID_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    id: int
    spec: TemplateRevisionSpec
    attachment: TemplateRevisionAttachment
    revision: _base_pb2.CreatedRevision
    def __init__(self, id: _Optional[int] = ..., spec: _Optional[_Union[TemplateRevisionSpec, _Mapping]] = ..., attachment: _Optional[_Union[TemplateRevisionAttachment, _Mapping]] = ..., revision: _Optional[_Union[_base_pb2.CreatedRevision, _Mapping]] = ...) -> None: ...

class TemplateRevisionSpec(_message.Message):
    __slots__ = ("revision_name", "revision_memo", "name", "path", "file_type", "file_mode", "permission", "content_spec")
    REVISION_NAME_FIELD_NUMBER: _ClassVar[int]
    REVISION_MEMO_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILE_MODE_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    CONTENT_SPEC_FIELD_NUMBER: _ClassVar[int]
    revision_name: str
    revision_memo: str
    name: str
    path: str
    file_type: str
    file_mode: str
    permission: _config_item_pb2.FilePermission
    content_spec: _content_pb2.ContentSpec
    def __init__(self, revision_name: _Optional[str] = ..., revision_memo: _Optional[str] = ..., name: _Optional[str] = ..., path: _Optional[str] = ..., file_type: _Optional[str] = ..., file_mode: _Optional[str] = ..., permission: _Optional[_Union[_config_item_pb2.FilePermission, _Mapping]] = ..., content_spec: _Optional[_Union[_content_pb2.ContentSpec, _Mapping]] = ...) -> None: ...

class TemplateRevisionAttachment(_message.Message):
    __slots__ = ("biz_id", "template_space_id", "template_id")
    BIZ_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    biz_id: int
    template_space_id: int
    template_id: int
    def __init__(self, biz_id: _Optional[int] = ..., template_space_id: _Optional[int] = ..., template_id: _Optional[int] = ...) -> None: ...

class TemplateRevisionNamesDetail(_message.Message):
    __slots__ = ("template_id", "template_name", "latest_template_revision_id", "template_revisions")
    class revision_names(_message.Message):
        __slots__ = ("template_revision_id", "template_revision_name", "template_revision_memo")
        TEMPLATE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_REVISION_NAME_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_REVISION_MEMO_FIELD_NUMBER: _ClassVar[int]
        template_revision_id: int
        template_revision_name: str
        template_revision_memo: str
        def __init__(self, template_revision_id: _Optional[int] = ..., template_revision_name: _Optional[str] = ..., template_revision_memo: _Optional[str] = ...) -> None: ...
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    LATEST_TEMPLATE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_REVISIONS_FIELD_NUMBER: _ClassVar[int]
    template_id: int
    template_name: str
    latest_template_revision_id: int
    template_revisions: _containers.RepeatedCompositeFieldContainer[TemplateRevisionNamesDetail.revision_names]
    def __init__(self, template_id: _Optional[int] = ..., template_name: _Optional[str] = ..., latest_template_revision_id: _Optional[int] = ..., template_revisions: _Optional[_Iterable[_Union[TemplateRevisionNamesDetail.revision_names, _Mapping]]] = ...) -> None: ...
