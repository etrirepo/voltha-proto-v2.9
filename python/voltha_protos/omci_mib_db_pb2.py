# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: voltha_protos/omci_mib_db.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='voltha_protos/omci_mib_db.proto',
  package='omci',
  syntax='proto3',
  serialized_options=b'\n\030org.opencord.voltha.omciZ,github.com/opencord/voltha-protos/v5/go/omci',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1fvoltha_protos/omci_mib_db.proto\x12\x04omci\"/\n\x10MibAttributeData\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"u\n\x0fMibInstanceData\x12\x13\n\x0binstance_id\x18\x01 \x01(\r\x12\x0f\n\x07\x63reated\x18\x02 \x01(\t\x12\x10\n\x08modified\x18\x03 \x01(\t\x12*\n\nattributes\x18\x04 \x03(\x0b\x32\x16.omci.MibAttributeData\"J\n\x0cMibClassData\x12\x10\n\x08\x63lass_id\x18\x01 \x01(\r\x12(\n\tinstances\x18\x02 \x03(\x0b\x32\x15.omci.MibInstanceData\"/\n\rManagedEntity\x12\x10\n\x08\x63lass_id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\"#\n\x0bMessageType\x12\x14\n\x0cmessage_type\x18\x01 \x01(\r\"\xf1\x01\n\rMibDeviceData\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12\x0f\n\x07\x63reated\x18\x02 \x01(\t\x12\x16\n\x0elast_sync_time\x18\x03 \x01(\t\x12\x15\n\rmib_data_sync\x18\x04 \x01(\r\x12\x0f\n\x07version\x18\x05 \x01(\r\x12#\n\x07\x63lasses\x18\x06 \x03(\x0b\x32\x12.omci.MibClassData\x12-\n\x10managed_entities\x18\x07 \x03(\x0b\x32\x13.omci.ManagedEntity\x12(\n\rmessage_types\x18\x08 \x03(\x0b\x32\x11.omci.MessageType\".\n\x11OpenOmciEventType\"\x19\n\x05Types\x12\x10\n\x0cstate_change\x10\x00\"J\n\rOpenOmciEvent\x12+\n\x04type\x18\x01 \x01(\x0e\x32\x1d.omci.OpenOmciEventType.Types\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\tBH\n\x18org.opencord.voltha.omciZ,github.com/opencord/voltha-protos/v5/go/omcib\x06proto3'
)



_OPENOMCIEVENTTYPE_TYPES = _descriptor.EnumDescriptor(
  name='Types',
  full_name='omci.OpenOmciEventType.Types',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='state_change', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=636,
  serialized_end=661,
)
_sym_db.RegisterEnumDescriptor(_OPENOMCIEVENTTYPE_TYPES)


_MIBATTRIBUTEDATA = _descriptor.Descriptor(
  name='MibAttributeData',
  full_name='omci.MibAttributeData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='omci.MibAttributeData.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='omci.MibAttributeData.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=41,
  serialized_end=88,
)


_MIBINSTANCEDATA = _descriptor.Descriptor(
  name='MibInstanceData',
  full_name='omci.MibInstanceData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='omci.MibInstanceData.instance_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created', full_name='omci.MibInstanceData.created', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='modified', full_name='omci.MibInstanceData.modified', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='omci.MibInstanceData.attributes', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=90,
  serialized_end=207,
)


_MIBCLASSDATA = _descriptor.Descriptor(
  name='MibClassData',
  full_name='omci.MibClassData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='class_id', full_name='omci.MibClassData.class_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instances', full_name='omci.MibClassData.instances', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=209,
  serialized_end=283,
)


_MANAGEDENTITY = _descriptor.Descriptor(
  name='ManagedEntity',
  full_name='omci.ManagedEntity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='class_id', full_name='omci.ManagedEntity.class_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='omci.ManagedEntity.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=285,
  serialized_end=332,
)


_MESSAGETYPE = _descriptor.Descriptor(
  name='MessageType',
  full_name='omci.MessageType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_type', full_name='omci.MessageType.message_type', index=0,
      number=1, type=13, cpp_type=3, label=1,
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
  serialized_start=334,
  serialized_end=369,
)


_MIBDEVICEDATA = _descriptor.Descriptor(
  name='MibDeviceData',
  full_name='omci.MibDeviceData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_id', full_name='omci.MibDeviceData.device_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created', full_name='omci.MibDeviceData.created', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_sync_time', full_name='omci.MibDeviceData.last_sync_time', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mib_data_sync', full_name='omci.MibDeviceData.mib_data_sync', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='omci.MibDeviceData.version', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='classes', full_name='omci.MibDeviceData.classes', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='managed_entities', full_name='omci.MibDeviceData.managed_entities', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message_types', full_name='omci.MibDeviceData.message_types', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=372,
  serialized_end=613,
)


_OPENOMCIEVENTTYPE = _descriptor.Descriptor(
  name='OpenOmciEventType',
  full_name='omci.OpenOmciEventType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _OPENOMCIEVENTTYPE_TYPES,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=615,
  serialized_end=661,
)


_OPENOMCIEVENT = _descriptor.Descriptor(
  name='OpenOmciEvent',
  full_name='omci.OpenOmciEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='omci.OpenOmciEvent.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='omci.OpenOmciEvent.data', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=663,
  serialized_end=737,
)

_MIBINSTANCEDATA.fields_by_name['attributes'].message_type = _MIBATTRIBUTEDATA
_MIBCLASSDATA.fields_by_name['instances'].message_type = _MIBINSTANCEDATA
_MIBDEVICEDATA.fields_by_name['classes'].message_type = _MIBCLASSDATA
_MIBDEVICEDATA.fields_by_name['managed_entities'].message_type = _MANAGEDENTITY
_MIBDEVICEDATA.fields_by_name['message_types'].message_type = _MESSAGETYPE
_OPENOMCIEVENTTYPE_TYPES.containing_type = _OPENOMCIEVENTTYPE
_OPENOMCIEVENT.fields_by_name['type'].enum_type = _OPENOMCIEVENTTYPE_TYPES
DESCRIPTOR.message_types_by_name['MibAttributeData'] = _MIBATTRIBUTEDATA
DESCRIPTOR.message_types_by_name['MibInstanceData'] = _MIBINSTANCEDATA
DESCRIPTOR.message_types_by_name['MibClassData'] = _MIBCLASSDATA
DESCRIPTOR.message_types_by_name['ManagedEntity'] = _MANAGEDENTITY
DESCRIPTOR.message_types_by_name['MessageType'] = _MESSAGETYPE
DESCRIPTOR.message_types_by_name['MibDeviceData'] = _MIBDEVICEDATA
DESCRIPTOR.message_types_by_name['OpenOmciEventType'] = _OPENOMCIEVENTTYPE
DESCRIPTOR.message_types_by_name['OpenOmciEvent'] = _OPENOMCIEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MibAttributeData = _reflection.GeneratedProtocolMessageType('MibAttributeData', (_message.Message,), {
  'DESCRIPTOR' : _MIBATTRIBUTEDATA,
  '__module__' : 'voltha_protos.omci_mib_db_pb2'
  # @@protoc_insertion_point(class_scope:omci.MibAttributeData)
  })
_sym_db.RegisterMessage(MibAttributeData)

MibInstanceData = _reflection.GeneratedProtocolMessageType('MibInstanceData', (_message.Message,), {
  'DESCRIPTOR' : _MIBINSTANCEDATA,
  '__module__' : 'voltha_protos.omci_mib_db_pb2'
  # @@protoc_insertion_point(class_scope:omci.MibInstanceData)
  })
_sym_db.RegisterMessage(MibInstanceData)

MibClassData = _reflection.GeneratedProtocolMessageType('MibClassData', (_message.Message,), {
  'DESCRIPTOR' : _MIBCLASSDATA,
  '__module__' : 'voltha_protos.omci_mib_db_pb2'
  # @@protoc_insertion_point(class_scope:omci.MibClassData)
  })
_sym_db.RegisterMessage(MibClassData)

ManagedEntity = _reflection.GeneratedProtocolMessageType('ManagedEntity', (_message.Message,), {
  'DESCRIPTOR' : _MANAGEDENTITY,
  '__module__' : 'voltha_protos.omci_mib_db_pb2'
  # @@protoc_insertion_point(class_scope:omci.ManagedEntity)
  })
_sym_db.RegisterMessage(ManagedEntity)

MessageType = _reflection.GeneratedProtocolMessageType('MessageType', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGETYPE,
  '__module__' : 'voltha_protos.omci_mib_db_pb2'
  # @@protoc_insertion_point(class_scope:omci.MessageType)
  })
_sym_db.RegisterMessage(MessageType)

MibDeviceData = _reflection.GeneratedProtocolMessageType('MibDeviceData', (_message.Message,), {
  'DESCRIPTOR' : _MIBDEVICEDATA,
  '__module__' : 'voltha_protos.omci_mib_db_pb2'
  # @@protoc_insertion_point(class_scope:omci.MibDeviceData)
  })
_sym_db.RegisterMessage(MibDeviceData)

OpenOmciEventType = _reflection.GeneratedProtocolMessageType('OpenOmciEventType', (_message.Message,), {
  'DESCRIPTOR' : _OPENOMCIEVENTTYPE,
  '__module__' : 'voltha_protos.omci_mib_db_pb2'
  # @@protoc_insertion_point(class_scope:omci.OpenOmciEventType)
  })
_sym_db.RegisterMessage(OpenOmciEventType)

OpenOmciEvent = _reflection.GeneratedProtocolMessageType('OpenOmciEvent', (_message.Message,), {
  'DESCRIPTOR' : _OPENOMCIEVENT,
  '__module__' : 'voltha_protos.omci_mib_db_pb2'
  # @@protoc_insertion_point(class_scope:omci.OpenOmciEvent)
  })
_sym_db.RegisterMessage(OpenOmciEvent)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
