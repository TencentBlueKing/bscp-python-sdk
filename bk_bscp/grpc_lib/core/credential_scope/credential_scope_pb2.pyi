from bk_bscp.grpc_lib.core.base import base_pb2 as _base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CredentialScopeAttachment(_message.Message):
    __slots__ = ("biz_id", "credential_id")
    BIZ_ID_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_ID_FIELD_NUMBER: _ClassVar[int]
    biz_id: int
    credential_id: int
    def __init__(self, biz_id: _Optional[int] = ..., credential_id: _Optional[int] = ...) -> None: ...

class CredentialScopeList(_message.Message):
    __slots__ = ("id", "spec", "attachment", "revision")
    ID_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    id: int
    spec: CredentialScopeSpec
    attachment: CredentialScopeAttachment
    revision: _base_pb2.Revision
    def __init__(self, id: _Optional[int] = ..., spec: _Optional[_Union[CredentialScopeSpec, _Mapping]] = ..., attachment: _Optional[_Union[CredentialScopeAttachment, _Mapping]] = ..., revision: _Optional[_Union[_base_pb2.Revision, _Mapping]] = ...) -> None: ...

class CredentialScopeSpec(_message.Message):
    __slots__ = ("app", "scope")
    APP_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    app: str
    scope: str
    def __init__(self, app: _Optional[str] = ..., scope: _Optional[str] = ...) -> None: ...

class UpdateScopeSpec(_message.Message):
    __slots__ = ("id", "app", "scope")
    ID_FIELD_NUMBER: _ClassVar[int]
    APP_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    app: str
    scope: str
    def __init__(self, id: _Optional[int] = ..., app: _Optional[str] = ..., scope: _Optional[str] = ...) -> None: ...
