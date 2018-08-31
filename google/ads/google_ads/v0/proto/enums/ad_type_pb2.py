# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/enums/ad_type.proto

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
  name='google/ads/googleads_v0/proto/enums/ad_type.proto',
  package='google.ads.googleads.v0.enums',
  syntax='proto3',
  serialized_pb=_b('\n1google/ads/googleads_v0/proto/enums/ad_type.proto\x12\x1dgoogle.ads.googleads.v0.enums\"\xe1\x01\n\nAdTypeEnum\"\xd2\x01\n\x06\x41\x64Type\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0b\n\x07TEXT_AD\x10\x02\x12\x14\n\x10\x45XPANDED_TEXT_AD\x10\x03\x12\x15\n\x11\x44YNAMIC_SEARCH_AD\x10\x04\x12\x19\n\x15RESPONSIVE_DISPLAY_AD\x10\x05\x12\x10\n\x0c\x43\x41LL_ONLY_AD\x10\x06\x12\x1e\n\x1a\x45XPANDED_DYNAMIC_SEARCH_AD\x10\x07\x12\x0c\n\x08HOTEL_AD\x10\x08\x12\x15\n\x11SHOPPING_SMART_AD\x10\tB\xbc\x01\n!com.google.ads.googleads.v0.enumsB\x0b\x41\x64TypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V0.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V0\\Enumsb\x06proto3')
)



_ADTYPEENUM_ADTYPE = _descriptor.EnumDescriptor(
  name='AdType',
  full_name='google.ads.googleads.v0.enums.AdTypeEnum.AdType',
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
      name='TEXT_AD', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPANDED_TEXT_AD', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DYNAMIC_SEARCH_AD', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESPONSIVE_DISPLAY_AD', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALL_ONLY_AD', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPANDED_DYNAMIC_SEARCH_AD', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOTEL_AD', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHOPPING_SMART_AD', index=9, number=9,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=100,
  serialized_end=310,
)
_sym_db.RegisterEnumDescriptor(_ADTYPEENUM_ADTYPE)


_ADTYPEENUM = _descriptor.Descriptor(
  name='AdTypeEnum',
  full_name='google.ads.googleads.v0.enums.AdTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ADTYPEENUM_ADTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=310,
)

_ADTYPEENUM_ADTYPE.containing_type = _ADTYPEENUM
DESCRIPTOR.message_types_by_name['AdTypeEnum'] = _ADTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdTypeEnum = _reflection.GeneratedProtocolMessageType('AdTypeEnum', (_message.Message,), dict(
  DESCRIPTOR = _ADTYPEENUM,
  __module__ = 'google.ads.googleads_v0.proto.enums.ad_type_pb2'
  ,
  __doc__ = """Container for enum describing possible types of an ad.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.enums.AdTypeEnum)
  ))
_sym_db.RegisterMessage(AdTypeEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!com.google.ads.googleads.v0.enumsB\013AdTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V0.Enums\312\002\035Google\\Ads\\GoogleAds\\V0\\Enums'))
# @@protoc_insertion_point(module_scope)
