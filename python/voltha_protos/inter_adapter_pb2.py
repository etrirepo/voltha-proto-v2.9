# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: voltha_protos/inter_adapter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from voltha_protos import common_pb2 as voltha__protos_dot_common__pb2
from voltha_protos import voltha_pb2 as voltha__protos_dot_voltha__pb2
try:
  voltha__protos_dot_common__pb2 = voltha__protos_dot_voltha__pb2.voltha__protos_dot_common__pb2
except AttributeError:
  voltha__protos_dot_common__pb2 = voltha__protos_dot_voltha__pb2.voltha_protos.common_pb2
from voltha_protos import tech_profile_pb2 as voltha__protos_dot_tech__profile__pb2
from voltha_protos import openolt_pb2 as voltha__protos_dot_openolt__pb2
from voltha_protos import device_pb2 as voltha__protos_dot_device__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='voltha_protos/inter_adapter.proto',
  package='inter_adapter',
  syntax='proto3',
  serialized_options=b'\n!org.opencord.voltha.inter_adapterZ5github.com/opencord/voltha-protos/v5/go/inter_adapter',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!voltha_protos/inter_adapter.proto\x12\rinter_adapter\x1a\x1avoltha_protos/common.proto\x1a\x1avoltha_protos/voltha.proto\x1a voltha_protos/tech_profile.proto\x1a\x1bvoltha_protos/openolt.proto\x1a\x1avoltha_protos/device.proto\"\xba\x01\n\x0bOmciMessage\x12\x0f\n\x07message\x18\x01 \x01(\x0c\x12\x33\n\x0e\x63onnect_status\x18\x02 \x01(\x0e\x32\x1b.common.ConnectStatus.Types\x12\x32\n\rproxy_address\x18\x03 \x01(\x0b\x32\x1b.device.Device.ProxyAddress\x12\x18\n\x10parent_device_id\x18\x04 \x01(\t\x12\x17\n\x0f\x63hild_device_id\x18\x05 \x01(\t\"\xea\x01\n\x1aTechProfileDownloadMessage\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12\x0e\n\x06uni_id\x18\x02 \x01(\r\x12\x18\n\x10tp_instance_path\x18\x03 \x01(\t\x12\x38\n\x0btp_instance\x18\x04 \x01(\x0b\x32!.tech_profile.TechProfileInstanceH\x00\x12\x41\n\x10\x65pon_tp_instance\x18\x05 \x01(\x0b\x32%.tech_profile.EponTechProfileInstanceH\x00\x42\x12\n\x10tech_tp_instance\"h\n\x14\x44\x65leteGemPortMessage\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12\x0e\n\x06uni_id\x18\x02 \x01(\r\x12\x18\n\x10tp_instance_path\x18\x03 \x01(\t\x12\x13\n\x0bgem_port_id\x18\x04 \x01(\r\"c\n\x12\x44\x65leteTcontMessage\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12\x0e\n\x06uni_id\x18\x02 \x01(\r\x12\x18\n\x10tp_instance_path\x18\x03 \x01(\t\x12\x10\n\x08\x61lloc_id\x18\x04 \x01(\r\"Y\n\x14OnuIndicationMessage\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12.\n\x0eonu_indication\x18\x02 \x01(\x0b\x32\x16.openolt.OnuIndication\"\xa3\x01\n!TechProfileInstanceRequestMessage\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12\x18\n\x10tp_instance_path\x18\x02 \x01(\t\x12\x18\n\x10parent_device_id\x18\x03 \x01(\t\x12\x17\n\x0fparent_pon_port\x18\x04 \x01(\r\x12\x0e\n\x06onu_id\x18\x05 \x01(\r\x12\x0e\n\x06uni_id\x18\x06 \x01(\rBZ\n!org.opencord.voltha.inter_adapterZ5github.com/opencord/voltha-protos/v5/go/inter_adapterb\x06proto3'
  ,
  dependencies=[voltha__protos_dot_common__pb2.DESCRIPTOR,voltha__protos_dot_voltha__pb2.DESCRIPTOR,voltha__protos_dot_tech__profile__pb2.DESCRIPTOR,voltha__protos_dot_openolt__pb2.DESCRIPTOR,voltha__protos_dot_device__pb2.DESCRIPTOR,])




_OMCIMESSAGE = _descriptor.Descriptor(
  name='OmciMessage',
  full_name='inter_adapter.OmciMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='inter_adapter.OmciMessage.message', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='connect_status', full_name='inter_adapter.OmciMessage.connect_status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proxy_address', full_name='inter_adapter.OmciMessage.proxy_address', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parent_device_id', full_name='inter_adapter.OmciMessage.parent_device_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='child_device_id', full_name='inter_adapter.OmciMessage.child_device_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=200,
  serialized_end=386,
)


_TECHPROFILEDOWNLOADMESSAGE = _descriptor.Descriptor(
  name='TechProfileDownloadMessage',
  full_name='inter_adapter.TechProfileDownloadMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_id', full_name='inter_adapter.TechProfileDownloadMessage.device_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uni_id', full_name='inter_adapter.TechProfileDownloadMessage.uni_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tp_instance_path', full_name='inter_adapter.TechProfileDownloadMessage.tp_instance_path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tp_instance', full_name='inter_adapter.TechProfileDownloadMessage.tp_instance', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='epon_tp_instance', full_name='inter_adapter.TechProfileDownloadMessage.epon_tp_instance', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='tech_tp_instance', full_name='inter_adapter.TechProfileDownloadMessage.tech_tp_instance',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=389,
  serialized_end=623,
)


_DELETEGEMPORTMESSAGE = _descriptor.Descriptor(
  name='DeleteGemPortMessage',
  full_name='inter_adapter.DeleteGemPortMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_id', full_name='inter_adapter.DeleteGemPortMessage.device_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uni_id', full_name='inter_adapter.DeleteGemPortMessage.uni_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tp_instance_path', full_name='inter_adapter.DeleteGemPortMessage.tp_instance_path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gem_port_id', full_name='inter_adapter.DeleteGemPortMessage.gem_port_id', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=625,
  serialized_end=729,
)


_DELETETCONTMESSAGE = _descriptor.Descriptor(
  name='DeleteTcontMessage',
  full_name='inter_adapter.DeleteTcontMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_id', full_name='inter_adapter.DeleteTcontMessage.device_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uni_id', full_name='inter_adapter.DeleteTcontMessage.uni_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tp_instance_path', full_name='inter_adapter.DeleteTcontMessage.tp_instance_path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='alloc_id', full_name='inter_adapter.DeleteTcontMessage.alloc_id', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=731,
  serialized_end=830,
)


_ONUINDICATIONMESSAGE = _descriptor.Descriptor(
  name='OnuIndicationMessage',
  full_name='inter_adapter.OnuIndicationMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_id', full_name='inter_adapter.OnuIndicationMessage.device_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='onu_indication', full_name='inter_adapter.OnuIndicationMessage.onu_indication', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=832,
  serialized_end=921,
)


_TECHPROFILEINSTANCEREQUESTMESSAGE = _descriptor.Descriptor(
  name='TechProfileInstanceRequestMessage',
  full_name='inter_adapter.TechProfileInstanceRequestMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_id', full_name='inter_adapter.TechProfileInstanceRequestMessage.device_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tp_instance_path', full_name='inter_adapter.TechProfileInstanceRequestMessage.tp_instance_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parent_device_id', full_name='inter_adapter.TechProfileInstanceRequestMessage.parent_device_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parent_pon_port', full_name='inter_adapter.TechProfileInstanceRequestMessage.parent_pon_port', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='onu_id', full_name='inter_adapter.TechProfileInstanceRequestMessage.onu_id', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uni_id', full_name='inter_adapter.TechProfileInstanceRequestMessage.uni_id', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=924,
  serialized_end=1087,
)

_OMCIMESSAGE.fields_by_name['connect_status'].enum_type = voltha__protos_dot_common__pb2._CONNECTSTATUS_TYPES
_OMCIMESSAGE.fields_by_name['proxy_address'].message_type = voltha__protos_dot_device__pb2._DEVICE_PROXYADDRESS
_TECHPROFILEDOWNLOADMESSAGE.fields_by_name['tp_instance'].message_type = voltha__protos_dot_tech__profile__pb2._TECHPROFILEINSTANCE
_TECHPROFILEDOWNLOADMESSAGE.fields_by_name['epon_tp_instance'].message_type = voltha__protos_dot_tech__profile__pb2._EPONTECHPROFILEINSTANCE
_TECHPROFILEDOWNLOADMESSAGE.oneofs_by_name['tech_tp_instance'].fields.append(
  _TECHPROFILEDOWNLOADMESSAGE.fields_by_name['tp_instance'])
_TECHPROFILEDOWNLOADMESSAGE.fields_by_name['tp_instance'].containing_oneof = _TECHPROFILEDOWNLOADMESSAGE.oneofs_by_name['tech_tp_instance']
_TECHPROFILEDOWNLOADMESSAGE.oneofs_by_name['tech_tp_instance'].fields.append(
  _TECHPROFILEDOWNLOADMESSAGE.fields_by_name['epon_tp_instance'])
_TECHPROFILEDOWNLOADMESSAGE.fields_by_name['epon_tp_instance'].containing_oneof = _TECHPROFILEDOWNLOADMESSAGE.oneofs_by_name['tech_tp_instance']
_ONUINDICATIONMESSAGE.fields_by_name['onu_indication'].message_type = voltha__protos_dot_openolt__pb2._ONUINDICATION
DESCRIPTOR.message_types_by_name['OmciMessage'] = _OMCIMESSAGE
DESCRIPTOR.message_types_by_name['TechProfileDownloadMessage'] = _TECHPROFILEDOWNLOADMESSAGE
DESCRIPTOR.message_types_by_name['DeleteGemPortMessage'] = _DELETEGEMPORTMESSAGE
DESCRIPTOR.message_types_by_name['DeleteTcontMessage'] = _DELETETCONTMESSAGE
DESCRIPTOR.message_types_by_name['OnuIndicationMessage'] = _ONUINDICATIONMESSAGE
DESCRIPTOR.message_types_by_name['TechProfileInstanceRequestMessage'] = _TECHPROFILEINSTANCEREQUESTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OmciMessage = _reflection.GeneratedProtocolMessageType('OmciMessage', (_message.Message,), {
  'DESCRIPTOR' : _OMCIMESSAGE,
  '__module__' : 'voltha_protos.inter_adapter_pb2'
  # @@protoc_insertion_point(class_scope:inter_adapter.OmciMessage)
  })
_sym_db.RegisterMessage(OmciMessage)

TechProfileDownloadMessage = _reflection.GeneratedProtocolMessageType('TechProfileDownloadMessage', (_message.Message,), {
  'DESCRIPTOR' : _TECHPROFILEDOWNLOADMESSAGE,
  '__module__' : 'voltha_protos.inter_adapter_pb2'
  # @@protoc_insertion_point(class_scope:inter_adapter.TechProfileDownloadMessage)
  })
_sym_db.RegisterMessage(TechProfileDownloadMessage)

DeleteGemPortMessage = _reflection.GeneratedProtocolMessageType('DeleteGemPortMessage', (_message.Message,), {
  'DESCRIPTOR' : _DELETEGEMPORTMESSAGE,
  '__module__' : 'voltha_protos.inter_adapter_pb2'
  # @@protoc_insertion_point(class_scope:inter_adapter.DeleteGemPortMessage)
  })
_sym_db.RegisterMessage(DeleteGemPortMessage)

DeleteTcontMessage = _reflection.GeneratedProtocolMessageType('DeleteTcontMessage', (_message.Message,), {
  'DESCRIPTOR' : _DELETETCONTMESSAGE,
  '__module__' : 'voltha_protos.inter_adapter_pb2'
  # @@protoc_insertion_point(class_scope:inter_adapter.DeleteTcontMessage)
  })
_sym_db.RegisterMessage(DeleteTcontMessage)

OnuIndicationMessage = _reflection.GeneratedProtocolMessageType('OnuIndicationMessage', (_message.Message,), {
  'DESCRIPTOR' : _ONUINDICATIONMESSAGE,
  '__module__' : 'voltha_protos.inter_adapter_pb2'
  # @@protoc_insertion_point(class_scope:inter_adapter.OnuIndicationMessage)
  })
_sym_db.RegisterMessage(OnuIndicationMessage)

TechProfileInstanceRequestMessage = _reflection.GeneratedProtocolMessageType('TechProfileInstanceRequestMessage', (_message.Message,), {
  'DESCRIPTOR' : _TECHPROFILEINSTANCEREQUESTMESSAGE,
  '__module__' : 'voltha_protos.inter_adapter_pb2'
  # @@protoc_insertion_point(class_scope:inter_adapter.TechProfileInstanceRequestMessage)
  })
_sym_db.RegisterMessage(TechProfileInstanceRequestMessage)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
