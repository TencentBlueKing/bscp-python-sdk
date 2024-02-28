from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TemplateBoundCounts(_message.Message):
    __slots__ = ("template_id", "bound_unnamed_app_count", "bound_named_app_count", "bound_template_set_count")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    BOUND_UNNAMED_APP_COUNT_FIELD_NUMBER: _ClassVar[int]
    BOUND_NAMED_APP_COUNT_FIELD_NUMBER: _ClassVar[int]
    BOUND_TEMPLATE_SET_COUNT_FIELD_NUMBER: _ClassVar[int]
    template_id: int
    bound_unnamed_app_count: int
    bound_named_app_count: int
    bound_template_set_count: int
    def __init__(self, template_id: _Optional[int] = ..., bound_unnamed_app_count: _Optional[int] = ..., bound_named_app_count: _Optional[int] = ..., bound_template_set_count: _Optional[int] = ...) -> None: ...

class TemplateRevisionBoundCounts(_message.Message):
    __slots__ = ("template_revision_id", "bound_unnamed_app_count", "bound_named_app_count")
    TEMPLATE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    BOUND_UNNAMED_APP_COUNT_FIELD_NUMBER: _ClassVar[int]
    BOUND_NAMED_APP_COUNT_FIELD_NUMBER: _ClassVar[int]
    template_revision_id: int
    bound_unnamed_app_count: int
    bound_named_app_count: int
    def __init__(self, template_revision_id: _Optional[int] = ..., bound_unnamed_app_count: _Optional[int] = ..., bound_named_app_count: _Optional[int] = ...) -> None: ...

class TemplateSetBoundCounts(_message.Message):
    __slots__ = ("template_set_id", "bound_unnamed_app_count", "bound_named_app_count")
    TEMPLATE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    BOUND_UNNAMED_APP_COUNT_FIELD_NUMBER: _ClassVar[int]
    BOUND_NAMED_APP_COUNT_FIELD_NUMBER: _ClassVar[int]
    template_set_id: int
    bound_unnamed_app_count: int
    bound_named_app_count: int
    def __init__(self, template_set_id: _Optional[int] = ..., bound_unnamed_app_count: _Optional[int] = ..., bound_named_app_count: _Optional[int] = ...) -> None: ...

class TemplateBoundUnnamedAppDetail(_message.Message):
    __slots__ = ("template_revision_id", "template_revision_name", "app_id", "app_name")
    TEMPLATE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_REVISION_NAME_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    APP_NAME_FIELD_NUMBER: _ClassVar[int]
    template_revision_id: int
    template_revision_name: str
    app_id: int
    app_name: str
    def __init__(self, template_revision_id: _Optional[int] = ..., template_revision_name: _Optional[str] = ..., app_id: _Optional[int] = ..., app_name: _Optional[str] = ...) -> None: ...

class TemplateBoundNamedAppDetail(_message.Message):
    __slots__ = ("template_revision_id", "template_revision_name", "app_id", "app_name", "release_id", "release_name")
    TEMPLATE_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_REVISION_NAME_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    APP_NAME_FIELD_NUMBER: _ClassVar[int]
    RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_NAME_FIELD_NUMBER: _ClassVar[int]
    template_revision_id: int
    template_revision_name: str
    app_id: int
    app_name: str
    release_id: int
    release_name: str
    def __init__(self, template_revision_id: _Optional[int] = ..., template_revision_name: _Optional[str] = ..., app_id: _Optional[int] = ..., app_name: _Optional[str] = ..., release_id: _Optional[int] = ..., release_name: _Optional[str] = ...) -> None: ...

class TemplateBoundTemplateSetDetail(_message.Message):
    __slots__ = ("template_set_id", "template_set_name")
    TEMPLATE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_SET_NAME_FIELD_NUMBER: _ClassVar[int]
    template_set_id: int
    template_set_name: str
    def __init__(self, template_set_id: _Optional[int] = ..., template_set_name: _Optional[str] = ...) -> None: ...

class MultiTemplateBoundTemplateSetDetail(_message.Message):
    __slots__ = ("template_id", "template_name", "template_set_id", "template_set_name")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_SET_NAME_FIELD_NUMBER: _ClassVar[int]
    template_id: int
    template_name: str
    template_set_id: int
    template_set_name: str
    def __init__(self, template_id: _Optional[int] = ..., template_name: _Optional[str] = ..., template_set_id: _Optional[int] = ..., template_set_name: _Optional[str] = ...) -> None: ...

class TemplateRevisionBoundUnnamedAppDetail(_message.Message):
    __slots__ = ("app_id", "app_name")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    APP_NAME_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    app_name: str
    def __init__(self, app_id: _Optional[int] = ..., app_name: _Optional[str] = ...) -> None: ...

class TemplateRevisionBoundNamedAppDetail(_message.Message):
    __slots__ = ("app_id", "app_name", "release_id", "release_name")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    APP_NAME_FIELD_NUMBER: _ClassVar[int]
    RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_NAME_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    app_name: str
    release_id: int
    release_name: str
    def __init__(self, app_id: _Optional[int] = ..., app_name: _Optional[str] = ..., release_id: _Optional[int] = ..., release_name: _Optional[str] = ...) -> None: ...

class TemplateSetBoundUnnamedAppDetail(_message.Message):
    __slots__ = ("app_id", "app_name")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    APP_NAME_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    app_name: str
    def __init__(self, app_id: _Optional[int] = ..., app_name: _Optional[str] = ...) -> None: ...

class MultiTemplateSetBoundUnnamedAppDetail(_message.Message):
    __slots__ = ("template_set_id", "template_set_name", "app_id", "app_name")
    TEMPLATE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_SET_NAME_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    APP_NAME_FIELD_NUMBER: _ClassVar[int]
    template_set_id: int
    template_set_name: str
    app_id: int
    app_name: str
    def __init__(self, template_set_id: _Optional[int] = ..., template_set_name: _Optional[str] = ..., app_id: _Optional[int] = ..., app_name: _Optional[str] = ...) -> None: ...

class TemplateSetBoundNamedAppDetail(_message.Message):
    __slots__ = ("app_id", "app_name", "release_id", "release_name")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    APP_NAME_FIELD_NUMBER: _ClassVar[int]
    RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_NAME_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    app_name: str
    release_id: int
    release_name: str
    def __init__(self, app_id: _Optional[int] = ..., app_name: _Optional[str] = ..., release_id: _Optional[int] = ..., release_name: _Optional[str] = ...) -> None: ...

class LatestTemplateBoundUnnamedAppDetail(_message.Message):
    __slots__ = ("template_set_id", "template_set_name", "app_id", "app_name")
    TEMPLATE_SET_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_SET_NAME_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    APP_NAME_FIELD_NUMBER: _ClassVar[int]
    template_set_id: int
    template_set_name: str
    app_id: int
    app_name: str
    def __init__(self, template_set_id: _Optional[int] = ..., template_set_name: _Optional[str] = ..., app_id: _Optional[int] = ..., app_name: _Optional[str] = ...) -> None: ...
