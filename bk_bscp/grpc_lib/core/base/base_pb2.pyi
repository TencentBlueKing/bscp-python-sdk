from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Revision(_message.Message):
    __slots__ = ("creator", "reviser", "create_at", "update_at")
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    REVISER_FIELD_NUMBER: _ClassVar[int]
    CREATE_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_AT_FIELD_NUMBER: _ClassVar[int]
    creator: str
    reviser: str
    create_at: str
    update_at: str
    def __init__(self, creator: _Optional[str] = ..., reviser: _Optional[str] = ..., create_at: _Optional[str] = ..., update_at: _Optional[str] = ...) -> None: ...

class CreatedRevision(_message.Message):
    __slots__ = ("creator", "create_at")
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    CREATE_AT_FIELD_NUMBER: _ClassVar[int]
    creator: str
    create_at: str
    def __init__(self, creator: _Optional[str] = ..., create_at: _Optional[str] = ...) -> None: ...

class BasePage(_message.Message):
    __slots__ = ("count", "start", "limit", "sort", "order")
    COUNT_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    count: bool
    start: int
    limit: int
    sort: str
    order: str
    def __init__(self, count: bool = ..., start: _Optional[int] = ..., limit: _Optional[int] = ..., sort: _Optional[str] = ..., order: _Optional[str] = ...) -> None: ...

class EmptyReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EmptyResp(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BaseResp(_message.Message):
    __slots__ = ("code", "message")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: str
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class Versioning(_message.Message):
    __slots__ = ("Major", "Minor", "Patch")
    MAJOR_FIELD_NUMBER: _ClassVar[int]
    MINOR_FIELD_NUMBER: _ClassVar[int]
    PATCH_FIELD_NUMBER: _ClassVar[int]
    Major: int
    Minor: int
    Patch: int
    def __init__(self, Major: _Optional[int] = ..., Minor: _Optional[int] = ..., Patch: _Optional[int] = ...) -> None: ...

class InvalidArgument(_message.Message):
    __slots__ = ("field", "message")
    FIELD_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    field: str
    message: str
    def __init__(self, field: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...
