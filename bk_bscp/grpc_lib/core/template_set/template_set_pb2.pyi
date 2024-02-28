from bk_bscp.grpc_lib.core.base import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TemplateSet(_message.Message):
    __slots__ = ("id", "spec", "attachment", "revision")
    ID_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    id: int
    spec: TemplateSetSpec
    attachment: TemplateSetAttachment
    revision: _base_pb2.Revision
    def __init__(self, id: _Optional[int] = ..., spec: _Optional[_Union[TemplateSetSpec, _Mapping]] = ..., attachment: _Optional[_Union[TemplateSetAttachment, _Mapping]] = ..., revision: _Optional[_Union[_base_pb2.Revision, _Mapping]] = ...) -> None: ...

class TemplateSetSpec(_message.Message):
    __slots__ = ("name", "memo", "template_ids", "public", "bound_apps")
    NAME_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_IDS_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    BOUND_APPS_FIELD_NUMBER: _ClassVar[int]
    name: str
    memo: str
    template_ids: _containers.RepeatedScalarFieldContainer[int]
    public: bool
    bound_apps: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, name: _Optional[str] = ..., memo: _Optional[str] = ..., template_ids: _Optional[_Iterable[int]] = ..., public: bool = ..., bound_apps: _Optional[_Iterable[int]] = ...) -> None: ...

class TemplateSetAttachment(_message.Message):
    __slots__ = ("biz_id", "template_space_id")
    BIZ_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    biz_id: int
    template_space_id: int
    def __init__(self, biz_id: _Optional[int] = ..., template_space_id: _Optional[int] = ...) -> None: ...

class TemplateSetOfBizDetail(_message.Message):
    __slots__ = ("template_space_id", "template_space_name", "template_sets")
    class TemplateSetOfBiz(_message.Message):
        __slots__ = ("template_set_id", "template_set_name", "template_ids")
        TEMPLATE_SET_ID_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_SET_NAME_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_IDS_FIELD_NUMBER: _ClassVar[int]
        template_set_id: int
        template_set_name: str
        template_ids: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, template_set_id: _Optional[int] = ..., template_set_name: _Optional[str] = ..., template_ids: _Optional[_Iterable[int]] = ...) -> None: ...
    TEMPLATE_SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_SPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_SETS_FIELD_NUMBER: _ClassVar[int]
    template_space_id: int
    template_space_name: str
    template_sets: _containers.RepeatedCompositeFieldContainer[TemplateSetOfBizDetail.TemplateSetOfBiz]
    def __init__(self, template_space_id: _Optional[int] = ..., template_space_name: _Optional[str] = ..., template_sets: _Optional[_Iterable[_Union[TemplateSetOfBizDetail.TemplateSetOfBiz, _Mapping]]] = ...) -> None: ...

class TemplateSetBriefInfo(_message.Message):
    __slots__ = ("template_space_id", "template_space_name", "template_set_id", "template_set_name")
    TEMPLATE_SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_SPACE_NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_SET_NAME_FIELD_NUMBER: _ClassVar[int]
    template_space_id: int
    template_space_name: str
    template_set_id: int
    template_set_name: str
    def __init__(self, template_space_id: _Optional[int] = ..., template_space_name: _Optional[str] = ..., template_set_id: _Optional[int] = ..., template_set_name: _Optional[str] = ...) -> None: ...
