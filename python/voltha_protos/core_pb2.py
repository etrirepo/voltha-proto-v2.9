# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: voltha_protos/core.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='voltha_protos/core.proto',
  package='core',
  syntax='proto3',
  serialized_options=b'\n\030org.opencord.voltha.coreZ,github.com/opencord/voltha-protos/v5/go/core',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18voltha_protos/core.proto\x12\x04\x63ore\"\xef\x01\n\x14\x44\x65viceTransientState\x12\x39\n\x0ftransient_state\x18\x01 \x01(\x0e\x32 .core.DeviceTransientState.Types\"\x9b\x01\n\x05Types\x12\x08\n\x04NONE\x10\x00\x12\x07\n\x03\x41NY\x10\x01\x12\x12\n\x0e\x46ORCE_DELETING\x10\x02\x12\x19\n\x15\x44\x45LETING_FROM_ADAPTER\x10\x03\x12\"\n\x1e\x44\x45LETING_POST_ADAPTER_RESPONSE\x10\x04\x12\x11\n\rDELETE_FAILED\x10\x05\x12\x19\n\x15RECONCILE_IN_PROGRESS\x10\x06\x42H\n\x18org.opencord.voltha.coreZ,github.com/opencord/voltha-protos/v5/go/coreb\x06proto3'
)



_DEVICETRANSIENTSTATE_TYPES = _descriptor.EnumDescriptor(
  name='Types',
  full_name='core.DeviceTransientState.Types',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ANY', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FORCE_DELETING', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DELETING_FROM_ADAPTER', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DELETING_POST_ADAPTER_RESPONSE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DELETE_FAILED', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RECONCILE_IN_PROGRESS', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=119,
  serialized_end=274,
)
_sym_db.RegisterEnumDescriptor(_DEVICETRANSIENTSTATE_TYPES)


_DEVICETRANSIENTSTATE = _descriptor.Descriptor(
  name='DeviceTransientState',
  full_name='core.DeviceTransientState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='transient_state', full_name='core.DeviceTransientState.transient_state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DEVICETRANSIENTSTATE_TYPES,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=274,
)

_DEVICETRANSIENTSTATE.fields_by_name['transient_state'].enum_type = _DEVICETRANSIENTSTATE_TYPES
_DEVICETRANSIENTSTATE_TYPES.containing_type = _DEVICETRANSIENTSTATE
DESCRIPTOR.message_types_by_name['DeviceTransientState'] = _DEVICETRANSIENTSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeviceTransientState = _reflection.GeneratedProtocolMessageType('DeviceTransientState', (_message.Message,), {
  'DESCRIPTOR' : _DEVICETRANSIENTSTATE,
  '__module__' : 'voltha_protos.core_pb2'
  # @@protoc_insertion_point(class_scope:core.DeviceTransientState)
  })
_sym_db.RegisterMessage(DeviceTransientState)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)