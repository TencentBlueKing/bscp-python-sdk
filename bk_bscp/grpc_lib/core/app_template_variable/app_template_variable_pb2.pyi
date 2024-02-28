from bk_bscp.grpc_lib.core.base import base_pb2 as _base_pb2
from bk_bscp.grpc_lib.core.template_variable import template_variable_pb2 as _template_variable_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AppTemplateVariable(_message.Message):
    __slots__ = ("id", "spec", "attachment", "revision")
    ID_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    id: int
    spec: AppTemplateVariableSpec
    attachment: AppTemplateVariableAttachment
    revision: _base_pb2.Revision
    def __init__(self, id: _Optional[int] = ..., spec: _Optional[_Union[AppTemplateVariableSpec, _Mapping]] = ..., attachment: _Optional[_Union[AppTemplateVariableAttachment, _Mapping]] = ..., revision: _Optional[_Union[_base_pb2.Revision, _Mapping]] = ...) -> None: ...

class AppTemplateVariableSpec(_message.Message):
    __slots__ = ("variables",)
    VARIABLES_FIELD_NUMBER: _ClassVar[int]
    variables: _containers.RepeatedCompositeFieldContainer[_template_variable_pb2.TemplateVariableSpec]
    def __init__(self, variables: _Optional[_Iterable[_Union[_template_variable_pb2.TemplateVariableSpec, _Mapping]]] = ...) -> None: ...

class AppTemplateVariableAttachment(_message.Message):
    __slots__ = ("biz_id", "app_id")
    BIZ_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    biz_id: int
    app_id: int
    def __init__(self, biz_id: _Optional[int] = ..., app_id: _Optional[int] = ...) -> None: ...

class AppTemplateVariableReference(_message.Message):
    __slots__ = ("variable_name", "references")
    class reference(_message.Message):
        __slots__ = ("id", "template_revision_id", "name", "path")
        ID_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        id: int
        template_revision_id: int
        name: str
        path: str
        def __init__(self, id: _Optional[int] = ..., template_revision_id: _Optional[int] = ..., name: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...
    VARIABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    REFERENCES_FIELD_NUMBER: _ClassVar[int]
    variable_name: str
    references: _containers.RepeatedCompositeFieldContainer[AppTemplateVariableReference.reference]
    def __init__(self, variable_name: _Optional[str] = ..., references: _Optional[_Iterable[_Union[AppTemplateVariableReference.reference, _Mapping]]] = ...) -> None: ...
