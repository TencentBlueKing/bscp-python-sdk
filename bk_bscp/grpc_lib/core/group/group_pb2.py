# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pkg/protocol/core/group/group.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from bk_bscp.grpc_lib.core.base import base_pb2 as pkg_dot_protocol_dot_core_dot_base_dot_base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#pkg/protocol/core/group/group.proto\x12\x07pbgroup\x1a\x1cgoogle/protobuf/struct.proto\x1a!pkg/protocol/core/base/base.proto\"\x87\x01\n\x05Group\x12\n\n\x02id\x18\x01 \x01(\r\x12 \n\x04spec\x18\x02 \x01(\x0b\x32\x12.pbgroup.GroupSpec\x12,\n\nattachment\x18\x03 \x01(\x0b\x32\x18.pbgroup.GroupAttachment\x12\"\n\x08revision\x18\x04 \x01(\x0b\x32\x10.pbbase.Revision\"\x82\x01\n\tGroupSpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06public\x18\x02 \x01(\x08\x12\x11\n\tbind_apps\x18\x03 \x03(\r\x12\x0c\n\x04mode\x18\x04 \x01(\t\x12)\n\x08selector\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0b\n\x03uid\x18\x06 \x01(\t\"!\n\x0fGroupAttachment\x12\x0e\n\x06\x62iz_id\x18\x01 \x01(\rBYZWgithub.com/TencentBlueKing/bk-bcs/bcs-services/bcs-bscp/pkg/protocol/core/group;pbgroupb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pkg.protocol.core.group.group_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZWgithub.com/TencentBlueKing/bk-bcs/bcs-services/bcs-bscp/pkg/protocol/core/group;pbgroup'
  _globals['_GROUP']._serialized_start=114
  _globals['_GROUP']._serialized_end=249
  _globals['_GROUPSPEC']._serialized_start=252
  _globals['_GROUPSPEC']._serialized_end=382
  _globals['_GROUPATTACHMENT']._serialized_start=384
  _globals['_GROUPATTACHMENT']._serialized_end=417
# @@protoc_insertion_point(module_scope)