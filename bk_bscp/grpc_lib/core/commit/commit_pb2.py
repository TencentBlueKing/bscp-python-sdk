# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pkg/protocol/core/commit/commit.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bk_bscp.grpc_lib.core.base import base_pb2 as pkg_dot_protocol_dot_core_dot_base_dot_base__pb2
from bk_bscp.grpc_lib.core.content import content_pb2 as pkg_dot_protocol_dot_core_dot_content_dot_content__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%pkg/protocol/core/commit/commit.proto\x12\x08pbcommit\x1a!pkg/protocol/core/base/base.proto\x1a\'pkg/protocol/core/content/content.proto\"\x93\x01\n\x06\x43ommit\x12\n\n\x02id\x18\x01 \x01(\r\x12\"\n\x04spec\x18\x02 \x01(\x0b\x32\x14.pbcommit.CommitSpec\x12.\n\nattachment\x18\x03 \x01(\x0b\x32\x1a.pbcommit.CommitAttachment\x12)\n\x08revision\x18\x04 \x01(\x0b\x32\x17.pbbase.CreatedRevision\"W\n\nCommitSpec\x12\x12\n\ncontent_id\x18\x01 \x01(\r\x12\'\n\x07\x63ontent\x18\x02 \x01(\x0b\x32\x16.pbcontent.ContentSpec\x12\x0c\n\x04memo\x18\x03 \x01(\t\"g\n\x12ReleasedCommitSpec\x12\x12\n\ncontent_id\x18\x01 \x01(\r\x12/\n\x07\x63ontent\x18\x02 \x01(\x0b\x32\x1e.pbcontent.ReleasedContentSpec\x12\x0c\n\x04memo\x18\x03 \x01(\t\"J\n\x10\x43ommitAttachment\x12\x0e\n\x06\x62iz_id\x18\x01 \x01(\r\x12\x0e\n\x06\x61pp_id\x18\x02 \x01(\r\x12\x16\n\x0e\x63onfig_item_id\x18\x03 \x01(\rB[ZYgithub.com/TencentBlueKing/bk-bcs/bcs-services/bcs-bscp/pkg/protocol/core/commit;pbcommitb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pkg.protocol.core.commit.commit_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZYgithub.com/TencentBlueKing/bk-bcs/bcs-services/bcs-bscp/pkg/protocol/core/commit;pbcommit'
  _globals['_COMMIT']._serialized_start=128
  _globals['_COMMIT']._serialized_end=275
  _globals['_COMMITSPEC']._serialized_start=277
  _globals['_COMMITSPEC']._serialized_end=364
  _globals['_RELEASEDCOMMITSPEC']._serialized_start=366
  _globals['_RELEASEDCOMMITSPEC']._serialized_end=469
  _globals['_COMMITATTACHMENT']._serialized_start=471
  _globals['_COMMITATTACHMENT']._serialized_end=545
# @@protoc_insertion_point(module_scope)
