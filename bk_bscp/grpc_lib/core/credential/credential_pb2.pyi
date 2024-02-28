from bk_bscp.grpc_lib.core.base import base_pb2 as _base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CredentialList(_message.Message):
    __slots__ = ("id", "spec", "attachment", "revision")
    ID_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    id: int
    spec: CredentialSpec
    attachment: CredentialAttachment
    revision: _base_pb2.Revision
    def __init__(self, id: _Optional[int] = ..., spec: _Optional[_Union[CredentialSpec, _Mapping]] = ..., attachment: _Optional[_Union[CredentialAttachment, _Mapping]] = ..., revision: _Optional[_Union[_base_pb2.Revision, _Mapping]] = ...) -> None: ...

class CredentialSpec(_message.Message):
    __slots__ = ("credential_type", "enc_credential", "enc_algorithm", "name", "memo", "enable")
    CREDENTIAL_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENC_CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    ENC_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    credential_type: str
    enc_credential: str
    enc_algorithm: str
    name: str
    memo: str
    enable: bool
    def __init__(self, credential_type: _Optional[str] = ..., enc_credential: _Optional[str] = ..., enc_algorithm: _Optional[str] = ..., name: _Optional[str] = ..., memo: _Optional[str] = ..., enable: bool = ...) -> None: ...

class CredentialAttachment(_message.Message):
    __slots__ = ("biz_id",)
    BIZ_ID_FIELD_NUMBER: _ClassVar[int]
    biz_id: int
    def __init__(self, biz_id: _Optional[int] = ...) -> None: ...

class CredentialScope(_message.Message):
    __slots__ = ("scope",)
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    scope: str
    def __init__(self, scope: _Optional[str] = ...) -> None: ...
