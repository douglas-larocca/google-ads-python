# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/enums/shared_set_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/enums/shared_set_type.proto',
  package='google.ads.googleads.v0.enums',
  syntax='proto3',
  serialized_pb=_b('\n9google/ads/googleads_v0/proto/enums/shared_set_type.proto\x12\x1dgoogle.ads.googleads.v0.enums\"r\n\x11SharedSetTypeEnum\"]\n\rSharedSetType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x15\n\x11NEGATIVE_KEYWORDS\x10\x02\x12\x17\n\x13NEGATIVE_PLACEMENTS\x10\x03\x42\xc3\x01\n!com.google.ads.googleads.v0.enumsB\x12SharedSetTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V0.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V0\\Enumsb\x06proto3')
)



_SHAREDSETTYPEENUM_SHAREDSETTYPE = _descriptor.EnumDescriptor(
  name='SharedSetType',
  full_name='google.ads.googleads.v0.enums.SharedSetTypeEnum.SharedSetType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEGATIVE_KEYWORDS', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEGATIVE_PLACEMENTS', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=113,
  serialized_end=206,
)
_sym_db.RegisterEnumDescriptor(_SHAREDSETTYPEENUM_SHAREDSETTYPE)


_SHAREDSETTYPEENUM = _descriptor.Descriptor(
  name='SharedSetTypeEnum',
  full_name='google.ads.googleads.v0.enums.SharedSetTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SHAREDSETTYPEENUM_SHAREDSETTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=92,
  serialized_end=206,
)

_SHAREDSETTYPEENUM_SHAREDSETTYPE.containing_type = _SHAREDSETTYPEENUM
DESCRIPTOR.message_types_by_name['SharedSetTypeEnum'] = _SHAREDSETTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SharedSetTypeEnum = _reflection.GeneratedProtocolMessageType('SharedSetTypeEnum', (_message.Message,), dict(
  DESCRIPTOR = _SHAREDSETTYPEENUM,
  __module__ = 'google.ads.googleads_v0.proto.enums.shared_set_type_pb2'
  ,
  __doc__ = """Container for enum describing types of shared sets.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.enums.SharedSetTypeEnum)
  ))
_sym_db.RegisterMessage(SharedSetTypeEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!com.google.ads.googleads.v0.enumsB\022SharedSetTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V0.Enums\312\002\035Google\\Ads\\GoogleAds\\V0\\Enums'))
# @@protoc_insertion_point(module_scope)
