# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/services/google_ads_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v0.proto.common import metrics_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_common_dot_metrics__pb2
from google.ads.google_ads.v0.proto.enums import ad_network_type_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_ad__network__type__pb2
from google.ads.google_ads.v0.proto.enums import day_of_week_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_day__of__week__pb2
from google.ads.google_ads.v0.proto.enums import device_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_device__pb2
from google.ads.google_ads.v0.proto.enums import month_of_year_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_month__of__year__pb2
from google.ads.google_ads.v0.proto.enums import slot_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_slot__pb2
from google.ads.google_ads.v0.proto.resources import ad_group_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_ad__group__pb2
from google.ads.google_ads.v0.proto.resources import ad_group_ad_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_ad__group__ad__pb2
from google.ads.google_ads.v0.proto.resources import ad_group_bid_modifier_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_ad__group__bid__modifier__pb2
from google.ads.google_ads.v0.proto.resources import ad_group_criterion_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_ad__group__criterion__pb2
from google.ads.google_ads.v0.proto.resources import bidding_strategy_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_bidding__strategy__pb2
from google.ads.google_ads.v0.proto.resources import campaign_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_campaign__pb2
from google.ads.google_ads.v0.proto.resources import campaign_bid_modifier_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_campaign__bid__modifier__pb2
from google.ads.google_ads.v0.proto.resources import campaign_budget_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_campaign__budget__pb2
from google.ads.google_ads.v0.proto.resources import campaign_criterion_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_campaign__criterion__pb2
from google.ads.google_ads.v0.proto.resources import campaign_group_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_campaign__group__pb2
from google.ads.google_ads.v0.proto.resources import campaign_shared_set_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_campaign__shared__set__pb2
from google.ads.google_ads.v0.proto.resources import customer_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_customer__pb2
from google.ads.google_ads.v0.proto.resources import geo_target_constant_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_geo__target__constant__pb2
from google.ads.google_ads.v0.proto.resources import keyword_view_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_keyword__view__pb2
from google.ads.google_ads.v0.proto.resources import recommendation_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_recommendation__pb2
from google.ads.google_ads.v0.proto.resources import shared_criterion_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_shared__criterion__pb2
from google.ads.google_ads.v0.proto.resources import shared_set_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_shared__set__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/services/google_ads_service.proto',
  package='google.ads.googleads.v0.services',
  syntax='proto3',
  serialized_pb=_b('\n?google/ads/googleads_v0/proto/services/google_ads_service.proto\x12 google.ads.googleads.v0.services\x1a\x32google/ads/googleads_v0/proto/common/metrics.proto\x1a\x39google/ads/googleads_v0/proto/enums/ad_network_type.proto\x1a\x35google/ads/googleads_v0/proto/enums/day_of_week.proto\x1a\x30google/ads/googleads_v0/proto/enums/device.proto\x1a\x37google/ads/googleads_v0/proto/enums/month_of_year.proto\x1a.google/ads/googleads_v0/proto/enums/slot.proto\x1a\x36google/ads/googleads_v0/proto/resources/ad_group.proto\x1a\x39google/ads/googleads_v0/proto/resources/ad_group_ad.proto\x1a\x43google/ads/googleads_v0/proto/resources/ad_group_bid_modifier.proto\x1a@google/ads/googleads_v0/proto/resources/ad_group_criterion.proto\x1a>google/ads/googleads_v0/proto/resources/bidding_strategy.proto\x1a\x36google/ads/googleads_v0/proto/resources/campaign.proto\x1a\x43google/ads/googleads_v0/proto/resources/campaign_bid_modifier.proto\x1a=google/ads/googleads_v0/proto/resources/campaign_budget.proto\x1a@google/ads/googleads_v0/proto/resources/campaign_criterion.proto\x1a<google/ads/googleads_v0/proto/resources/campaign_group.proto\x1a\x41google/ads/googleads_v0/proto/resources/campaign_shared_set.proto\x1a\x36google/ads/googleads_v0/proto/resources/customer.proto\x1a\x41google/ads/googleads_v0/proto/resources/geo_target_constant.proto\x1a:google/ads/googleads_v0/proto/resources/keyword_view.proto\x1a<google/ads/googleads_v0/proto/resources/recommendation.proto\x1a>google/ads/googleads_v0/proto/resources/shared_criterion.proto\x1a\x38google/ads/googleads_v0/proto/resources/shared_set.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1egoogle/protobuf/wrappers.proto\"c\n\x16SearchGoogleAdsRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12\r\n\x05query\x18\x02 \x01(\t\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05\"\xc0\x01\n\x17SearchGoogleAdsResponse\x12?\n\x07results\x18\x01 \x03(\x0b\x32..google.ads.googleads.v0.services.GoogleAdsRow\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x1b\n\x13total_results_count\x18\x03 \x01(\x03\x12.\n\nfield_mask\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\xc3\x0f\n\x0cGoogleAdsRow\x12<\n\x08\x61\x64_group\x18\x03 \x01(\x0b\x32*.google.ads.googleads.v0.resources.AdGroup\x12\x41\n\x0b\x61\x64_group_ad\x18\x10 \x01(\x0b\x32,.google.ads.googleads.v0.resources.AdGroupAd\x12T\n\x15\x61\x64_group_bid_modifier\x18\x18 \x01(\x0b\x32\x35.google.ads.googleads.v0.resources.AdGroupBidModifier\x12O\n\x12\x61\x64_group_criterion\x18\x11 \x01(\x0b\x32\x33.google.ads.googleads.v0.resources.AdGroupCriterion\x12L\n\x10\x62idding_strategy\x18\x12 \x01(\x0b\x32\x32.google.ads.googleads.v0.resources.BiddingStrategy\x12J\n\x0f\x63\x61mpaign_budget\x18\x13 \x01(\x0b\x32\x31.google.ads.googleads.v0.resources.CampaignBudget\x12=\n\x08\x63\x61mpaign\x18\x02 \x01(\x0b\x32+.google.ads.googleads.v0.resources.Campaign\x12U\n\x15\x63\x61mpaign_bid_modifier\x18\x1a \x01(\x0b\x32\x36.google.ads.googleads.v0.resources.CampaignBidModifier\x12P\n\x12\x63\x61mpaign_criterion\x18\x14 \x01(\x0b\x32\x34.google.ads.googleads.v0.resources.CampaignCriterion\x12H\n\x0e\x63\x61mpaign_group\x18\x19 \x01(\x0b\x32\x30.google.ads.googleads.v0.resources.CampaignGroup\x12Q\n\x13\x63\x61mpaign_shared_set\x18\x1e \x01(\x0b\x32\x34.google.ads.googleads.v0.resources.CampaignSharedSet\x12=\n\x08\x63ustomer\x18\x01 \x01(\x0b\x32+.google.ads.googleads.v0.resources.Customer\x12Q\n\x13geo_target_constant\x18\x17 \x01(\x0b\x32\x34.google.ads.googleads.v0.resources.GeoTargetConstant\x12\x44\n\x0ckeyword_view\x18\x15 \x01(\x0b\x32..google.ads.googleads.v0.resources.KeywordView\x12I\n\x0erecommendation\x18\x16 \x01(\x0b\x32\x31.google.ads.googleads.v0.resources.Recommendation\x12L\n\x10shared_criterion\x18\x1d \x01(\x0b\x32\x32.google.ads.googleads.v0.resources.SharedCriterion\x12@\n\nshared_set\x18\x1b \x01(\x0b\x32,.google.ads.googleads.v0.resources.SharedSet\x12\x38\n\x07metrics\x18\x04 \x01(\x0b\x32\'.google.ads.googleads.v0.common.Metrics\x12W\n\x0f\x61\x64_network_type\x18\x05 \x01(\x0e\x32>.google.ads.googleads.v0.enums.AdNetworkTypeEnum.AdNetworkType\x12*\n\x04\x64\x61te\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12K\n\x0b\x64\x61y_of_week\x18\x07 \x01(\x0e\x32\x36.google.ads.googleads.v0.enums.DayOfWeekEnum.DayOfWeek\x12@\n\x06\x64\x65vice\x18\x08 \x01(\x0e\x32\x30.google.ads.googleads.v0.enums.DeviceEnum.Device\x12)\n\x04hour\x18\t \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12+\n\x05month\x18\n \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12Q\n\rmonth_of_year\x18\x1c \x01(\x0e\x32:.google.ads.googleads.v0.enums.MonthOfYearEnum.MonthOfYear\x12-\n\x07quarter\x18\x0c \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12:\n\x04slot\x18\r \x01(\x0e\x32,.google.ads.googleads.v0.enums.SlotEnum.Slot\x12*\n\x04week\x18\x0e \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12)\n\x04year\x18\x0f \x01(\x0b\x32\x1b.google.protobuf.Int32Value2\xcd\x01\n\x10GoogleAdsService\x12\xb8\x01\n\x06Search\x12\x38.google.ads.googleads.v0.services.SearchGoogleAdsRequest\x1a\x39.google.ads.googleads.v0.services.SearchGoogleAdsResponse\"9\x82\xd3\xe4\x93\x02\x33\"./v0/customers/{customer_id=*}/googleAds:search:\x01*B\xd5\x01\n$com.google.ads.googleads.v0.servicesB\x15GoogleAdsServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V0.Services\xca\x02 Google\\Ads\\GoogleAds\\V0\\Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v0_dot_proto_dot_common_dot_metrics__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_ad__network__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_day__of__week__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_device__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_month__of__year__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_slot__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_ad__group__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_ad__group__ad__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_ad__group__bid__modifier__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_ad__group__criterion__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_bidding__strategy__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_campaign__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_campaign__bid__modifier__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_campaign__budget__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_campaign__criterion__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_campaign__group__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_campaign__shared__set__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_customer__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_geo__target__constant__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_keyword__view__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_recommendation__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_shared__criterion__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_shared__set__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_SEARCHGOOGLEADSREQUEST = _descriptor.Descriptor(
  name='SearchGoogleAdsRequest',
  full_name='google.ads.googleads.v0.services.SearchGoogleAdsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v0.services.SearchGoogleAdsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query', full_name='google.ads.googleads.v0.services.SearchGoogleAdsRequest.query', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.ads.googleads.v0.services.SearchGoogleAdsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.ads.googleads.v0.services.SearchGoogleAdsRequest.page_size', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1582,
  serialized_end=1681,
)


_SEARCHGOOGLEADSRESPONSE = _descriptor.Descriptor(
  name='SearchGoogleAdsResponse',
  full_name='google.ads.googleads.v0.services.SearchGoogleAdsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v0.services.SearchGoogleAdsResponse.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.ads.googleads.v0.services.SearchGoogleAdsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_results_count', full_name='google.ads.googleads.v0.services.SearchGoogleAdsResponse.total_results_count', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='field_mask', full_name='google.ads.googleads.v0.services.SearchGoogleAdsResponse.field_mask', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1684,
  serialized_end=1876,
)


_GOOGLEADSROW = _descriptor.Descriptor(
  name='GoogleAdsRow',
  full_name='google.ads.googleads.v0.services.GoogleAdsRow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ad_group', full_name='google.ads.googleads.v0.services.GoogleAdsRow.ad_group', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ad_group_ad', full_name='google.ads.googleads.v0.services.GoogleAdsRow.ad_group_ad', index=1,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ad_group_bid_modifier', full_name='google.ads.googleads.v0.services.GoogleAdsRow.ad_group_bid_modifier', index=2,
      number=24, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ad_group_criterion', full_name='google.ads.googleads.v0.services.GoogleAdsRow.ad_group_criterion', index=3,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bidding_strategy', full_name='google.ads.googleads.v0.services.GoogleAdsRow.bidding_strategy', index=4,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='campaign_budget', full_name='google.ads.googleads.v0.services.GoogleAdsRow.campaign_budget', index=5,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='campaign', full_name='google.ads.googleads.v0.services.GoogleAdsRow.campaign', index=6,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='campaign_bid_modifier', full_name='google.ads.googleads.v0.services.GoogleAdsRow.campaign_bid_modifier', index=7,
      number=26, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='campaign_criterion', full_name='google.ads.googleads.v0.services.GoogleAdsRow.campaign_criterion', index=8,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='campaign_group', full_name='google.ads.googleads.v0.services.GoogleAdsRow.campaign_group', index=9,
      number=25, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='campaign_shared_set', full_name='google.ads.googleads.v0.services.GoogleAdsRow.campaign_shared_set', index=10,
      number=30, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='customer', full_name='google.ads.googleads.v0.services.GoogleAdsRow.customer', index=11,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='geo_target_constant', full_name='google.ads.googleads.v0.services.GoogleAdsRow.geo_target_constant', index=12,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyword_view', full_name='google.ads.googleads.v0.services.GoogleAdsRow.keyword_view', index=13,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recommendation', full_name='google.ads.googleads.v0.services.GoogleAdsRow.recommendation', index=14,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shared_criterion', full_name='google.ads.googleads.v0.services.GoogleAdsRow.shared_criterion', index=15,
      number=29, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shared_set', full_name='google.ads.googleads.v0.services.GoogleAdsRow.shared_set', index=16,
      number=27, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metrics', full_name='google.ads.googleads.v0.services.GoogleAdsRow.metrics', index=17,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ad_network_type', full_name='google.ads.googleads.v0.services.GoogleAdsRow.ad_network_type', index=18,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date', full_name='google.ads.googleads.v0.services.GoogleAdsRow.date', index=19,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='day_of_week', full_name='google.ads.googleads.v0.services.GoogleAdsRow.day_of_week', index=20,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device', full_name='google.ads.googleads.v0.services.GoogleAdsRow.device', index=21,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hour', full_name='google.ads.googleads.v0.services.GoogleAdsRow.hour', index=22,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='month', full_name='google.ads.googleads.v0.services.GoogleAdsRow.month', index=23,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='month_of_year', full_name='google.ads.googleads.v0.services.GoogleAdsRow.month_of_year', index=24,
      number=28, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quarter', full_name='google.ads.googleads.v0.services.GoogleAdsRow.quarter', index=25,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slot', full_name='google.ads.googleads.v0.services.GoogleAdsRow.slot', index=26,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='week', full_name='google.ads.googleads.v0.services.GoogleAdsRow.week', index=27,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='year', full_name='google.ads.googleads.v0.services.GoogleAdsRow.year', index=28,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1879,
  serialized_end=3866,
)

_SEARCHGOOGLEADSRESPONSE.fields_by_name['results'].message_type = _GOOGLEADSROW
_SEARCHGOOGLEADSRESPONSE.fields_by_name['field_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_GOOGLEADSROW.fields_by_name['ad_group'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_ad__group__pb2._ADGROUP
_GOOGLEADSROW.fields_by_name['ad_group_ad'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_ad__group__ad__pb2._ADGROUPAD
_GOOGLEADSROW.fields_by_name['ad_group_bid_modifier'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_ad__group__bid__modifier__pb2._ADGROUPBIDMODIFIER
_GOOGLEADSROW.fields_by_name['ad_group_criterion'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_ad__group__criterion__pb2._ADGROUPCRITERION
_GOOGLEADSROW.fields_by_name['bidding_strategy'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_bidding__strategy__pb2._BIDDINGSTRATEGY
_GOOGLEADSROW.fields_by_name['campaign_budget'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_campaign__budget__pb2._CAMPAIGNBUDGET
_GOOGLEADSROW.fields_by_name['campaign'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_campaign__pb2._CAMPAIGN
_GOOGLEADSROW.fields_by_name['campaign_bid_modifier'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_campaign__bid__modifier__pb2._CAMPAIGNBIDMODIFIER
_GOOGLEADSROW.fields_by_name['campaign_criterion'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_campaign__criterion__pb2._CAMPAIGNCRITERION
_GOOGLEADSROW.fields_by_name['campaign_group'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_campaign__group__pb2._CAMPAIGNGROUP
_GOOGLEADSROW.fields_by_name['campaign_shared_set'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_campaign__shared__set__pb2._CAMPAIGNSHAREDSET
_GOOGLEADSROW.fields_by_name['customer'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_customer__pb2._CUSTOMER
_GOOGLEADSROW.fields_by_name['geo_target_constant'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_geo__target__constant__pb2._GEOTARGETCONSTANT
_GOOGLEADSROW.fields_by_name['keyword_view'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_keyword__view__pb2._KEYWORDVIEW
_GOOGLEADSROW.fields_by_name['recommendation'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_recommendation__pb2._RECOMMENDATION
_GOOGLEADSROW.fields_by_name['shared_criterion'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_shared__criterion__pb2._SHAREDCRITERION
_GOOGLEADSROW.fields_by_name['shared_set'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_shared__set__pb2._SHAREDSET
_GOOGLEADSROW.fields_by_name['metrics'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_common_dot_metrics__pb2._METRICS
_GOOGLEADSROW.fields_by_name['ad_network_type'].enum_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_ad__network__type__pb2._ADNETWORKTYPEENUM_ADNETWORKTYPE
_GOOGLEADSROW.fields_by_name['date'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_GOOGLEADSROW.fields_by_name['day_of_week'].enum_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_day__of__week__pb2._DAYOFWEEKENUM_DAYOFWEEK
_GOOGLEADSROW.fields_by_name['device'].enum_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_device__pb2._DEVICEENUM_DEVICE
_GOOGLEADSROW.fields_by_name['hour'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_GOOGLEADSROW.fields_by_name['month'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_GOOGLEADSROW.fields_by_name['month_of_year'].enum_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_month__of__year__pb2._MONTHOFYEARENUM_MONTHOFYEAR
_GOOGLEADSROW.fields_by_name['quarter'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_GOOGLEADSROW.fields_by_name['slot'].enum_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_slot__pb2._SLOTENUM_SLOT
_GOOGLEADSROW.fields_by_name['week'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_GOOGLEADSROW.fields_by_name['year'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
DESCRIPTOR.message_types_by_name['SearchGoogleAdsRequest'] = _SEARCHGOOGLEADSREQUEST
DESCRIPTOR.message_types_by_name['SearchGoogleAdsResponse'] = _SEARCHGOOGLEADSRESPONSE
DESCRIPTOR.message_types_by_name['GoogleAdsRow'] = _GOOGLEADSROW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchGoogleAdsRequest = _reflection.GeneratedProtocolMessageType('SearchGoogleAdsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHGOOGLEADSREQUEST,
  __module__ = 'google.ads.googleads_v0.proto.services.google_ads_service_pb2'
  ,
  __doc__ = """Request message for
  [GoogleAdsService.Search][google.ads.googleads.v0.services.GoogleAdsService.Search].
  
  
  Attributes:
      customer_id:
          The ID of the customer being queried.
      query:
          The query string.
      page_token:
          Token of the page to retrieve. If not specified, the first
          page of results will be returned. Use the value obtained from
          ``next_page_token`` in the previous response in order to
          request the next page of results.
      page_size:
          Number of elements to retrieve in a single page. When too
          large a page is requested, the server may decide to further
          limit the number of returned resources.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.SearchGoogleAdsRequest)
  ))
_sym_db.RegisterMessage(SearchGoogleAdsRequest)

SearchGoogleAdsResponse = _reflection.GeneratedProtocolMessageType('SearchGoogleAdsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHGOOGLEADSRESPONSE,
  __module__ = 'google.ads.googleads_v0.proto.services.google_ads_service_pb2'
  ,
  __doc__ = """Response message for
  [GoogleAdsService.Search][google.ads.googleads.v0.services.GoogleAdsService.Search].
  
  
  Attributes:
      results:
          The list of rows that matched the query.
      next_page_token:
          Pagination token used to retrieve the next page of results.
          Pass the content of this string as the ``page_token``
          attribute of the next request. ``next_page_token`` is not
          returned for the last page.
      total_results_count:
          Total number of results that match the query ignoring the
          LIMIT clause.
      field_mask:
          FieldMask that represents what fields were requested by the
          user.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.SearchGoogleAdsResponse)
  ))
_sym_db.RegisterMessage(SearchGoogleAdsResponse)

GoogleAdsRow = _reflection.GeneratedProtocolMessageType('GoogleAdsRow', (_message.Message,), dict(
  DESCRIPTOR = _GOOGLEADSROW,
  __module__ = 'google.ads.googleads_v0.proto.services.google_ads_service_pb2'
  ,
  __doc__ = """A returned row from the query.
  
  
  Attributes:
      ad_group:
          The ad group referenced in the query.
      ad_group_ad:
          The ad referenced in the query.
      ad_group_bid_modifier:
          The bid modifier referenced in the query.
      ad_group_criterion:
          The criterion referenced in the query.
      bidding_strategy:
          The bidding strategy referenced in the query.
      campaign_budget:
          The campaign budget referenced in the query.
      campaign:
          The campaign referenced in the query.
      campaign_bid_modifier:
          The campaign bid modifier referenced in the query.
      campaign_criterion:
          The campaign criterion referenced in the query.
      campaign_group:
          Campaign Group referenced in AWQL query.
      campaign_shared_set:
          Campaign Shared Set referenced in AWQL query.
      customer:
          The customer referenced in the query.
      geo_target_constant:
          The geo target constant referenced in the query.
      keyword_view:
          The keyword view referenced in the query.
      recommendation:
          The recommendation referenced in the query.
      shared_criterion:
          The shared set referenced in the query.
      shared_set:
          The shared set referenced in the query.
      metrics:
          The metrics.
      ad_network_type:
          Ad network type.
      date:
          Date to which metrics apply. YYYY-MM-DD format, e.g.,
          2018-04-17.
      day_of_week:
          Day of the week, e.g., MONDAY.
      device:
          Device to which metrics apply.
      hour:
          Hour of day as a number between 0 and 23, inclusive.
      month:
          Month as represented by the date of the first day of a month.
      month_of_year:
          Month of the year, e.g., January.
      quarter:
          Quarter as represented by the date of the first day of a
          quarter. Uses the calendar year for quarters, e.g., the second
          quarter of 2018 starts on 2018-04-01.
      slot:
          Position of the ad.
      week:
          Week as defined as Monday through Sunday, and represented by
          the date of Monday.
      year:
          Year, formatted as yyyy.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.GoogleAdsRow)
  ))
_sym_db.RegisterMessage(GoogleAdsRow)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n$com.google.ads.googleads.v0.servicesB\025GoogleAdsServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V0.Services\312\002 Google\\Ads\\GoogleAds\\V0\\Services'))

_GOOGLEADSSERVICE = _descriptor.ServiceDescriptor(
  name='GoogleAdsService',
  full_name='google.ads.googleads.v0.services.GoogleAdsService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=3869,
  serialized_end=4074,
  methods=[
  _descriptor.MethodDescriptor(
    name='Search',
    full_name='google.ads.googleads.v0.services.GoogleAdsService.Search',
    index=0,
    containing_service=None,
    input_type=_SEARCHGOOGLEADSREQUEST,
    output_type=_SEARCHGOOGLEADSRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\0023\"./v0/customers/{customer_id=*}/googleAds:search:\001*')),
  ),
])
_sym_db.RegisterServiceDescriptor(_GOOGLEADSSERVICE)

DESCRIPTOR.services_by_name['GoogleAdsService'] = _GOOGLEADSSERVICE

# @@protoc_insertion_point(module_scope)
