# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: LogTas1.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import common_pb2
import PublicTas1_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='LogTas1.proto',
  package='LogTas1',
  serialized_pb='\n\rLogTas1.proto\x12\x07LogTas1\x1a\x0c\x63ommon.proto\x1a\x10PublicTas1.proto\"\xf2\x02\n\x11QueryHisSysLogReq\x12\x1c\n\x06Header\x18\x01 \x01(\x0b\x32\x0c.MessageHead\x12#\n\x08PageInfo\x18\x02 \x01(\x0b\x32\x11.QueryReqPageInfo\x12\x0f\n\x07\x46unCode\x18\x03 \x03(\x05\x12\x13\n\x0b\x46unCodeFlag\x18\x04 \x01(\x05\x12\x12\n\nOperatorId\x18\x05 \x01(\t\x12\x16\n\x0eOperatorIdFlag\x18\x06 \x01(\x05\x12\n\n\x02Ip\x18\x07 \x01(\t\x12\x0e\n\x06IpFlag\x18\x08 \x01(\x05\x12\x13\n\x0bOperaObject\x18\t \x01(\t\x12\x17\n\x0fOperaObjectFlag\x18\n \x01(\x05\x12\x11\n\tStartDate\x18\x0b \x01(\t\x12\x15\n\rStartDateFlag\x18\x0c \x01(\x05\x12\x0f\n\x07\x45ndDate\x18\r \x01(\t\x12\x13\n\x0b\x45ndDateFlag\x18\x0e \x01(\x05\x12\x14\n\x0cOperatorType\x18\x0f \x01(\x05\x12\x18\n\x10OperatorTypeFlag\x18\x10 \x01(\x05\"\xa4\x01\n\x12QueryHisSysLogRsp_\x12\x0f\n\x07\x46unCode\x18\x01 \x01(\x05\x12\x12\n\nOperatorId\x18\x02 \x01(\t\x12\n\n\x02Ip\x18\x03 \x01(\t\x12\x13\n\x0bOperaObject\x18\x04 \x01(\t\x12\x11\n\tOperaDate\x18\x05 \x01(\t\x12\x0e\n\x06Status\x18\x06 \x01(\x05\x12\x0f\n\x07\x43ontent\x18\x07 \x01(\x0c\x12\x14\n\x0cOperatorType\x18\x08 \x01(\x05\"\xa3\x01\n\x11QueryHisSysLogRsp\x12\x1c\n\x06Header\x18\x01 \x01(\x0b\x32\x0c.MessageHead\x12\x0f\n\x07RetCode\x18\x02 \x01(\x05\x12\x0f\n\x07RetDesc\x18\x03 \x01(\t\x12#\n\x08PageInfo\x18\x04 \x01(\x0b\x32\x11.QueryRspPageInfo\x12)\n\x04Rsps\x18\x05 \x03(\x0b\x32\x1b.LogTas1.QueryHisSysLogRsp_\"\xf8\x01\n\x0f\x41\x64\x64HisSysLogReq\x12\x1c\n\x06Header\x18\x01 \x01(\x0b\x32\x0c.MessageHead\x12\x0f\n\x07\x46unCode\x18\x02 \x01(\x05\x12\x12\n\nOperatorId\x18\x03 \x01(\t\x12\n\n\x02Ip\x18\x04 \x01(\t\x12\x13\n\x0bOperaObject\x18\x05 \x01(\t\x12\x11\n\tOperaDate\x18\x06 \x01(\t\x12\x0e\n\x06Status\x18\x07 \x01(\x05\x12\x0f\n\x07\x43ontent\x18\x08 \x01(\t\x12\x11\n\tRequestID\x18\t \x01(\x05\x12\x13\n\x0b\x41\x63\x63ountCode\x18\n \x01(\t\x12\x0f\n\x07MsgName\x18\x0b \x01(\t\x12\x14\n\x0cOperatorType\x18\x0c \x01(\x05\"`\n\x0f\x41\x64\x64HisSysLogRsp\x12\x1c\n\x06Header\x18\x01 \x01(\x0b\x32\x0c.MessageHead\x12\x0f\n\x07RetCode\x18\x02 \x01(\x05\x12\x0f\n\x07RetDesc\x18\x03 \x01(\t\x12\r\n\x05LogID\x18\x04 \x01(\x05')




_QUERYHISSYSLOGREQ = _descriptor.Descriptor(
  name='QueryHisSysLogReq',
  full_name='LogTas1.QueryHisSysLogReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Header', full_name='LogTas1.QueryHisSysLogReq.Header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PageInfo', full_name='LogTas1.QueryHisSysLogReq.PageInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FunCode', full_name='LogTas1.QueryHisSysLogReq.FunCode', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FunCodeFlag', full_name='LogTas1.QueryHisSysLogReq.FunCodeFlag', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OperatorId', full_name='LogTas1.QueryHisSysLogReq.OperatorId', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OperatorIdFlag', full_name='LogTas1.QueryHisSysLogReq.OperatorIdFlag', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Ip', full_name='LogTas1.QueryHisSysLogReq.Ip', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='IpFlag', full_name='LogTas1.QueryHisSysLogReq.IpFlag', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OperaObject', full_name='LogTas1.QueryHisSysLogReq.OperaObject', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OperaObjectFlag', full_name='LogTas1.QueryHisSysLogReq.OperaObjectFlag', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StartDate', full_name='LogTas1.QueryHisSysLogReq.StartDate', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StartDateFlag', full_name='LogTas1.QueryHisSysLogReq.StartDateFlag', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='EndDate', full_name='LogTas1.QueryHisSysLogReq.EndDate', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='EndDateFlag', full_name='LogTas1.QueryHisSysLogReq.EndDateFlag', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OperatorType', full_name='LogTas1.QueryHisSysLogReq.OperatorType', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OperatorTypeFlag', full_name='LogTas1.QueryHisSysLogReq.OperatorTypeFlag', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=59,
  serialized_end=429,
)


_QUERYHISSYSLOGRSP_ = _descriptor.Descriptor(
  name='QueryHisSysLogRsp_',
  full_name='LogTas1.QueryHisSysLogRsp_',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='FunCode', full_name='LogTas1.QueryHisSysLogRsp_.FunCode', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OperatorId', full_name='LogTas1.QueryHisSysLogRsp_.OperatorId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Ip', full_name='LogTas1.QueryHisSysLogRsp_.Ip', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OperaObject', full_name='LogTas1.QueryHisSysLogRsp_.OperaObject', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OperaDate', full_name='LogTas1.QueryHisSysLogRsp_.OperaDate', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Status', full_name='LogTas1.QueryHisSysLogRsp_.Status', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Content', full_name='LogTas1.QueryHisSysLogRsp_.Content', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OperatorType', full_name='LogTas1.QueryHisSysLogRsp_.OperatorType', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=432,
  serialized_end=596,
)


_QUERYHISSYSLOGRSP = _descriptor.Descriptor(
  name='QueryHisSysLogRsp',
  full_name='LogTas1.QueryHisSysLogRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Header', full_name='LogTas1.QueryHisSysLogRsp.Header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RetCode', full_name='LogTas1.QueryHisSysLogRsp.RetCode', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RetDesc', full_name='LogTas1.QueryHisSysLogRsp.RetDesc', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PageInfo', full_name='LogTas1.QueryHisSysLogRsp.PageInfo', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Rsps', full_name='LogTas1.QueryHisSysLogRsp.Rsps', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=599,
  serialized_end=762,
)


_ADDHISSYSLOGREQ = _descriptor.Descriptor(
  name='AddHisSysLogReq',
  full_name='LogTas1.AddHisSysLogReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Header', full_name='LogTas1.AddHisSysLogReq.Header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FunCode', full_name='LogTas1.AddHisSysLogReq.FunCode', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OperatorId', full_name='LogTas1.AddHisSysLogReq.OperatorId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Ip', full_name='LogTas1.AddHisSysLogReq.Ip', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OperaObject', full_name='LogTas1.AddHisSysLogReq.OperaObject', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OperaDate', full_name='LogTas1.AddHisSysLogReq.OperaDate', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Status', full_name='LogTas1.AddHisSysLogReq.Status', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Content', full_name='LogTas1.AddHisSysLogReq.Content', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RequestID', full_name='LogTas1.AddHisSysLogReq.RequestID', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AccountCode', full_name='LogTas1.AddHisSysLogReq.AccountCode', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MsgName', full_name='LogTas1.AddHisSysLogReq.MsgName', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OperatorType', full_name='LogTas1.AddHisSysLogReq.OperatorType', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=765,
  serialized_end=1013,
)


_ADDHISSYSLOGRSP = _descriptor.Descriptor(
  name='AddHisSysLogRsp',
  full_name='LogTas1.AddHisSysLogRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Header', full_name='LogTas1.AddHisSysLogRsp.Header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RetCode', full_name='LogTas1.AddHisSysLogRsp.RetCode', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RetDesc', full_name='LogTas1.AddHisSysLogRsp.RetDesc', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LogID', full_name='LogTas1.AddHisSysLogRsp.LogID', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1015,
  serialized_end=1111,
)

_QUERYHISSYSLOGREQ.fields_by_name['Header'].message_type = common_pb2._MESSAGEHEAD
_QUERYHISSYSLOGREQ.fields_by_name['PageInfo'].message_type = common_pb2._QUERYREQPAGEINFO
_QUERYHISSYSLOGRSP.fields_by_name['Header'].message_type = common_pb2._MESSAGEHEAD
_QUERYHISSYSLOGRSP.fields_by_name['PageInfo'].message_type = common_pb2._QUERYRSPPAGEINFO
_QUERYHISSYSLOGRSP.fields_by_name['Rsps'].message_type = _QUERYHISSYSLOGRSP_
_ADDHISSYSLOGREQ.fields_by_name['Header'].message_type = common_pb2._MESSAGEHEAD
_ADDHISSYSLOGRSP.fields_by_name['Header'].message_type = common_pb2._MESSAGEHEAD
DESCRIPTOR.message_types_by_name['QueryHisSysLogReq'] = _QUERYHISSYSLOGREQ
DESCRIPTOR.message_types_by_name['QueryHisSysLogRsp_'] = _QUERYHISSYSLOGRSP_
DESCRIPTOR.message_types_by_name['QueryHisSysLogRsp'] = _QUERYHISSYSLOGRSP
DESCRIPTOR.message_types_by_name['AddHisSysLogReq'] = _ADDHISSYSLOGREQ
DESCRIPTOR.message_types_by_name['AddHisSysLogRsp'] = _ADDHISSYSLOGRSP

class QueryHisSysLogReq(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUERYHISSYSLOGREQ

  # @@protoc_insertion_point(class_scope:LogTas1.QueryHisSysLogReq)

class QueryHisSysLogRsp_(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUERYHISSYSLOGRSP_

  # @@protoc_insertion_point(class_scope:LogTas1.QueryHisSysLogRsp_)

class QueryHisSysLogRsp(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUERYHISSYSLOGRSP

  # @@protoc_insertion_point(class_scope:LogTas1.QueryHisSysLogRsp)

class AddHisSysLogReq(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ADDHISSYSLOGREQ

  # @@protoc_insertion_point(class_scope:LogTas1.AddHisSysLogReq)

class AddHisSysLogRsp(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ADDHISSYSLOGRSP

  # @@protoc_insertion_point(class_scope:LogTas1.AddHisSysLogRsp)


# @@protoc_insertion_point(module_scope)