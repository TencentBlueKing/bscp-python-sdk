from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Client(_message.Message):
    __slots__ = ("id", "spec", "attachment", "message_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    spec: ClientSpec
    attachment: ClientAttachment
    message_type: str
    def __init__(self, id: _Optional[int] = ..., spec: _Optional[_Union[ClientSpec, _Mapping]] = ..., attachment: _Optional[_Union[ClientAttachment, _Mapping]] = ..., message_type: _Optional[str] = ...) -> None: ...

class ClientSpec(_message.Message):
    __slots__ = ("client_version", "ip", "labels", "annotations", "first_connect_time", "last_heartbeat_time", "online_status", "resource", "current_release_id", "target_release_id", "release_change_status", "release_change_failed_reason", "failed_detail_reason", "client_type", "current_release_name", "specific_failed_reason")
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    FIRST_CONNECT_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_HEARTBEAT_TIME_FIELD_NUMBER: _ClassVar[int]
    ONLINE_STATUS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_CHANGE_STATUS_FIELD_NUMBER: _ClassVar[int]
    RELEASE_CHANGE_FAILED_REASON_FIELD_NUMBER: _ClassVar[int]
    FAILED_DETAIL_REASON_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_RELEASE_NAME_FIELD_NUMBER: _ClassVar[int]
    SPECIFIC_FAILED_REASON_FIELD_NUMBER: _ClassVar[int]
    client_version: str
    ip: str
    labels: str
    annotations: str
    first_connect_time: _timestamp_pb2.Timestamp
    last_heartbeat_time: _timestamp_pb2.Timestamp
    online_status: str
    resource: ClientResource
    current_release_id: int
    target_release_id: int
    release_change_status: str
    release_change_failed_reason: str
    failed_detail_reason: str
    client_type: str
    current_release_name: str
    specific_failed_reason: str
    def __init__(self, client_version: _Optional[str] = ..., ip: _Optional[str] = ..., labels: _Optional[str] = ..., annotations: _Optional[str] = ..., first_connect_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_heartbeat_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., online_status: _Optional[str] = ..., resource: _Optional[_Union[ClientResource, _Mapping]] = ..., current_release_id: _Optional[int] = ..., target_release_id: _Optional[int] = ..., release_change_status: _Optional[str] = ..., release_change_failed_reason: _Optional[str] = ..., failed_detail_reason: _Optional[str] = ..., client_type: _Optional[str] = ..., current_release_name: _Optional[str] = ..., specific_failed_reason: _Optional[str] = ...) -> None: ...

class ClientAttachment(_message.Message):
    __slots__ = ("uid", "biz_id", "app_id")
    UID_FIELD_NUMBER: _ClassVar[int]
    BIZ_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    uid: str
    biz_id: int
    app_id: int
    def __init__(self, uid: _Optional[str] = ..., biz_id: _Optional[int] = ..., app_id: _Optional[int] = ...) -> None: ...

class ClientResource(_message.Message):
    __slots__ = ("cpu_usage", "cpu_max_usage", "cpu_min_usage", "cpu_avg_usage", "memory_usage", "memory_max_usage", "memory_min_usage", "memory_avg_usage")
    CPU_USAGE_FIELD_NUMBER: _ClassVar[int]
    CPU_MAX_USAGE_FIELD_NUMBER: _ClassVar[int]
    CPU_MIN_USAGE_FIELD_NUMBER: _ClassVar[int]
    CPU_AVG_USAGE_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
    MEMORY_MAX_USAGE_FIELD_NUMBER: _ClassVar[int]
    MEMORY_MIN_USAGE_FIELD_NUMBER: _ClassVar[int]
    MEMORY_AVG_USAGE_FIELD_NUMBER: _ClassVar[int]
    cpu_usage: float
    cpu_max_usage: float
    cpu_min_usage: float
    cpu_avg_usage: float
    memory_usage: int
    memory_max_usage: int
    memory_min_usage: int
    memory_avg_usage: int
    def __init__(self, cpu_usage: _Optional[float] = ..., cpu_max_usage: _Optional[float] = ..., cpu_min_usage: _Optional[float] = ..., cpu_avg_usage: _Optional[float] = ..., memory_usage: _Optional[int] = ..., memory_max_usage: _Optional[int] = ..., memory_min_usage: _Optional[int] = ..., memory_avg_usage: _Optional[int] = ...) -> None: ...

class ClientQueryCondition(_message.Message):
    __slots__ = ("uid", "ip", "label", "current_release_name", "target_release_name", "release_change_status", "annotations", "online_status", "client_version", "client_type")
    UID_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    CURRENT_RELEASE_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_RELEASE_NAME_FIELD_NUMBER: _ClassVar[int]
    RELEASE_CHANGE_STATUS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    ONLINE_STATUS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    uid: str
    ip: str
    label: _struct_pb2.Struct
    current_release_name: str
    target_release_name: str
    release_change_status: _containers.RepeatedScalarFieldContainer[str]
    annotations: _struct_pb2.Struct
    online_status: _containers.RepeatedScalarFieldContainer[str]
    client_version: str
    client_type: str
    def __init__(self, uid: _Optional[str] = ..., ip: _Optional[str] = ..., label: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., current_release_name: _Optional[str] = ..., target_release_name: _Optional[str] = ..., release_change_status: _Optional[_Iterable[str]] = ..., annotations: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., online_status: _Optional[_Iterable[str]] = ..., client_version: _Optional[str] = ..., client_type: _Optional[str] = ...) -> None: ...

class ClientCommonReq(_message.Message):
    __slots__ = ("biz_id", "app_id", "search", "last_heartbeat_time", "pull_time")
    BIZ_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    LAST_HEARTBEAT_TIME_FIELD_NUMBER: _ClassVar[int]
    PULL_TIME_FIELD_NUMBER: _ClassVar[int]
    biz_id: int
    app_id: int
    search: ClientQueryCondition
    last_heartbeat_time: int
    pull_time: int
    def __init__(self, biz_id: _Optional[int] = ..., app_id: _Optional[int] = ..., search: _Optional[_Union[ClientQueryCondition, _Mapping]] = ..., last_heartbeat_time: _Optional[int] = ..., pull_time: _Optional[int] = ...) -> None: ...
