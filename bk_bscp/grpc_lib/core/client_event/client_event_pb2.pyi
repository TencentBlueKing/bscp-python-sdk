from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClientEvent(_message.Message):
    __slots__ = ("id", "spec", "attachment", "heartbeat_time", "message_type", "original_release_name", "target_release_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    SPEC_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_TIME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_RELEASE_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_RELEASE_NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    spec: ClientEventSpec
    attachment: ClientEventAttachment
    heartbeat_time: _timestamp_pb2.Timestamp
    message_type: str
    original_release_name: str
    target_release_name: str
    def __init__(self, id: _Optional[int] = ..., spec: _Optional[_Union[ClientEventSpec, _Mapping]] = ..., attachment: _Optional[_Union[ClientEventAttachment, _Mapping]] = ..., heartbeat_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., message_type: _Optional[str] = ..., original_release_name: _Optional[str] = ..., target_release_name: _Optional[str] = ...) -> None: ...

class ClientEventSpec(_message.Message):
    __slots__ = ("original_release_id", "target_release_id", "start_time", "end_time", "total_seconds", "total_file_size", "download_file_size", "total_file_num", "download_file_num", "release_change_status", "release_change_failed_reason", "failed_detail_reason", "specific_failed_reason")
    ORIGINAL_RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FILE_NUM_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_FILE_NUM_FIELD_NUMBER: _ClassVar[int]
    RELEASE_CHANGE_STATUS_FIELD_NUMBER: _ClassVar[int]
    RELEASE_CHANGE_FAILED_REASON_FIELD_NUMBER: _ClassVar[int]
    FAILED_DETAIL_REASON_FIELD_NUMBER: _ClassVar[int]
    SPECIFIC_FAILED_REASON_FIELD_NUMBER: _ClassVar[int]
    original_release_id: int
    target_release_id: int
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    total_seconds: float
    total_file_size: float
    download_file_size: float
    total_file_num: int
    download_file_num: int
    release_change_status: str
    release_change_failed_reason: str
    failed_detail_reason: str
    specific_failed_reason: str
    def __init__(self, original_release_id: _Optional[int] = ..., target_release_id: _Optional[int] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., total_seconds: _Optional[float] = ..., total_file_size: _Optional[float] = ..., download_file_size: _Optional[float] = ..., total_file_num: _Optional[int] = ..., download_file_num: _Optional[int] = ..., release_change_status: _Optional[str] = ..., release_change_failed_reason: _Optional[str] = ..., failed_detail_reason: _Optional[str] = ..., specific_failed_reason: _Optional[str] = ...) -> None: ...

class ClientEventAttachment(_message.Message):
    __slots__ = ("client_id", "uid", "biz_id", "app_id", "client_mode", "cursor_id")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    BIZ_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_MODE_FIELD_NUMBER: _ClassVar[int]
    CURSOR_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: int
    uid: str
    biz_id: int
    app_id: int
    client_mode: str
    cursor_id: str
    def __init__(self, client_id: _Optional[int] = ..., uid: _Optional[str] = ..., biz_id: _Optional[int] = ..., app_id: _Optional[int] = ..., client_mode: _Optional[str] = ..., cursor_id: _Optional[str] = ...) -> None: ...
