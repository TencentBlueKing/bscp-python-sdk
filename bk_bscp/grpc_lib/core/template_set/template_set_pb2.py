# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pkg/protocol/core/template-set/template_set.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bk_bscp.grpc_lib.core.base import base_pb2 as pkg_dot_protocol_dot_core_dot_base_dot_base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1pkg/protocol/core/template-set/template_set.proto\x12\x06pbtset\x1a!pkg/protocol/core/base/base.proto\"\x97\x01\n\x0bTemplateSet\x12\n\n\x02id\x18\x01 \x01(\r\x12%\n\x04spec\x18\x02 \x01(\x0b\x32\x17.pbtset.TemplateSetSpec\x12\x31\n\nattachment\x18\x03 \x01(\x0b\x32\x1d.pbtset.TemplateSetAttachment\x12\"\n\x08revision\x18\x04 \x01(\x0b\x32\x10.pbbase.Revision\"g\n\x0fTemplateSetSpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04memo\x18\x02 \x01(\t\x12\x14\n\x0ctemplate_ids\x18\x03 \x03(\r\x12\x0e\n\x06public\x18\x04 \x01(\x08\x12\x12\n\nbound_apps\x18\x05 \x03(\r\"B\n\x15TemplateSetAttachment\x12\x0e\n\x06\x62iz_id\x18\x01 \x01(\r\x12\x19\n\x11template_space_id\x18\x02 \x01(\r\"\xf6\x01\n\x16TemplateSetOfBizDetail\x12\x19\n\x11template_space_id\x18\x01 \x01(\r\x12\x1b\n\x13template_space_name\x18\x02 \x01(\t\x12\x46\n\rtemplate_sets\x18\x03 \x03(\x0b\x32/.pbtset.TemplateSetOfBizDetail.TemplateSetOfBiz\x1a\\\n\x10TemplateSetOfBiz\x12\x17\n\x0ftemplate_set_id\x18\x01 \x01(\r\x12\x19\n\x11template_set_name\x18\x02 \x01(\t\x12\x14\n\x0ctemplate_ids\x18\x03 \x03(\r\"\x82\x01\n\x14TemplateSetBriefInfo\x12\x19\n\x11template_space_id\x18\x01 \x01(\r\x12\x1b\n\x13template_space_name\x18\x02 \x01(\t\x12\x17\n\x0ftemplate_set_id\x18\x03 \x01(\r\x12\x19\n\x11template_set_name\x18\x04 \x01(\tB_Z]github.com/TencentBlueKing/bk-bcs/bcs-services/bcs-bscp/pkg/protocol/core/template-set;pbtsetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pkg.protocol.core.template_set.template_set_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z]github.com/TencentBlueKing/bk-bcs/bcs-services/bcs-bscp/pkg/protocol/core/template-set;pbtset'
  _globals['_TEMPLATESET']._serialized_start=97
  _globals['_TEMPLATESET']._serialized_end=248
  _globals['_TEMPLATESETSPEC']._serialized_start=250
  _globals['_TEMPLATESETSPEC']._serialized_end=353
  _globals['_TEMPLATESETATTACHMENT']._serialized_start=355
  _globals['_TEMPLATESETATTACHMENT']._serialized_end=421
  _globals['_TEMPLATESETOFBIZDETAIL']._serialized_start=424
  _globals['_TEMPLATESETOFBIZDETAIL']._serialized_end=670
  _globals['_TEMPLATESETOFBIZDETAIL_TEMPLATESETOFBIZ']._serialized_start=578
  _globals['_TEMPLATESETOFBIZDETAIL_TEMPLATESETOFBIZ']._serialized_end=670
  _globals['_TEMPLATESETBRIEFINFO']._serialized_start=673
  _globals['_TEMPLATESETBRIEFINFO']._serialized_end=803
# @@protoc_insertion_point(module_scope)