# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: voltha_protos/ietf_interfaces.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='voltha_protos/ietf_interfaces.proto',
  package='ietf',
  syntax='proto3',
  serialized_options=b'\n\030org.opencord.voltha.ietfZ,github.com/opencord/voltha-protos/v5/go/ietf',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#voltha_protos/ietf_interfaces.proto\x12\x04ietf\"5\n\nInterfaces\x12\'\n\x0e\x61ll_interfaces\x18\x01 \x03(\x0b\x32\x0f.ietf.Interface\"\xda\x01\n\tInterface\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x04 \x01(\x08\x12J\n\x18link_up_down_trap_enable\x18\x05 \x01(\x0e\x32(.ietf.Interface.LinkUpDownTrapEnableType\"?\n\x18LinkUpDownTrapEnableType\x12\x11\n\rTRAP_DISABLED\x10\x00\x12\x10\n\x0cTRAP_ENABLED\x10\x01\">\n\x0fInterfacesState\x12+\n\rall_interfacs\x18\x01 \x03(\x0b\x32\x14.ietf.InterfaceState\"\xd5\x03\n\x0eInterfaceState\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12:\n\x0c\x61\x64min_status\x18\x03 \x01(\x0e\x32$.ietf.InterfaceState.AdminStatusType\x12\x38\n\x0boper_status\x18\x04 \x01(\x0e\x32#.ietf.InterfaceState.OperStatusType\x12\x13\n\x0blast_change\x18\x05 \x01(\t\x12\x10\n\x08if_index\x18\x06 \x01(\x05\x12\x14\n\x0cphys_address\x18\x07 \x01(\t\x12\x17\n\x0fhigher_layer_if\x18\x08 \x03(\t\x12\x16\n\x0elower_layer_if\x18\t \x03(\t\x12\r\n\x05speed\x18\n \x01(\x04\"B\n\x0f\x41\x64minStatusType\x12\x0e\n\nADMIN_DOWN\x10\x00\x12\x11\n\rADMIN_TESTING\x10\x01\x12\x0c\n\x08\x41\x44MIN_UP\x10\x02\"p\n\x0eOperStatusType\x12\x0b\n\x07\x44ORMANT\x10\x00\x12\x14\n\x10LOWER_LAYER_DOWN\x10\x01\x12\x0b\n\x07UNKNOWN\x10\x02\x12\x0b\n\x07TESTING\x10\x03\x12\x06\n\x02UP\x10\x04\x12\x08\n\x04\x44OWN\x10\x05\x12\x0f\n\x0bNOT_PRESENT\x10\x06\x42H\n\x18org.opencord.voltha.ietfZ,github.com/opencord/voltha-protos/v5/go/ietfb\x06proto3'
)



_INTERFACE_LINKUPDOWNTRAPENABLETYPE = _descriptor.EnumDescriptor(
  name='LinkUpDownTrapEnableType',
  full_name='ietf.Interface.LinkUpDownTrapEnableType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TRAP_DISABLED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TRAP_ENABLED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=256,
  serialized_end=319,
)
_sym_db.RegisterEnumDescriptor(_INTERFACE_LINKUPDOWNTRAPENABLETYPE)

_INTERFACESTATE_ADMINSTATUSTYPE = _descriptor.EnumDescriptor(
  name='AdminStatusType',
  full_name='ietf.InterfaceState.AdminStatusType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ADMIN_DOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADMIN_TESTING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADMIN_UP', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=675,
  serialized_end=741,
)
_sym_db.RegisterEnumDescriptor(_INTERFACESTATE_ADMINSTATUSTYPE)

_INTERFACESTATE_OPERSTATUSTYPE = _descriptor.EnumDescriptor(
  name='OperStatusType',
  full_name='ietf.InterfaceState.OperStatusType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DORMANT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOWER_LAYER_DOWN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TESTING', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UP', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DOWN', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_PRESENT', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=743,
  serialized_end=855,
)
_sym_db.RegisterEnumDescriptor(_INTERFACESTATE_OPERSTATUSTYPE)


_INTERFACES = _descriptor.Descriptor(
  name='Interfaces',
  full_name='ietf.Interfaces',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='all_interfaces', full_name='ietf.Interfaces.all_interfaces', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=45,
  serialized_end=98,
)


_INTERFACE = _descriptor.Descriptor(
  name='Interface',
  full_name='ietf.Interface',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ietf.Interface.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='ietf.Interface.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='ietf.Interface.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='ietf.Interface.enabled', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='link_up_down_trap_enable', full_name='ietf.Interface.link_up_down_trap_enable', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _INTERFACE_LINKUPDOWNTRAPENABLETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=319,
)


_INTERFACESSTATE = _descriptor.Descriptor(
  name='InterfacesState',
  full_name='ietf.InterfacesState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='all_interfacs', full_name='ietf.InterfacesState.all_interfacs', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=321,
  serialized_end=383,
)


_INTERFACESTATE = _descriptor.Descriptor(
  name='InterfaceState',
  full_name='ietf.InterfaceState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ietf.InterfaceState.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='ietf.InterfaceState.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='admin_status', full_name='ietf.InterfaceState.admin_status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='oper_status', full_name='ietf.InterfaceState.oper_status', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_change', full_name='ietf.InterfaceState.last_change', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='if_index', full_name='ietf.InterfaceState.if_index', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phys_address', full_name='ietf.InterfaceState.phys_address', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='higher_layer_if', full_name='ietf.InterfaceState.higher_layer_if', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lower_layer_if', full_name='ietf.InterfaceState.lower_layer_if', index=8,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='speed', full_name='ietf.InterfaceState.speed', index=9,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _INTERFACESTATE_ADMINSTATUSTYPE,
    _INTERFACESTATE_OPERSTATUSTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=386,
  serialized_end=855,
)

_INTERFACES.fields_by_name['all_interfaces'].message_type = _INTERFACE
_INTERFACE.fields_by_name['link_up_down_trap_enable'].enum_type = _INTERFACE_LINKUPDOWNTRAPENABLETYPE
_INTERFACE_LINKUPDOWNTRAPENABLETYPE.containing_type = _INTERFACE
_INTERFACESSTATE.fields_by_name['all_interfacs'].message_type = _INTERFACESTATE
_INTERFACESTATE.fields_by_name['admin_status'].enum_type = _INTERFACESTATE_ADMINSTATUSTYPE
_INTERFACESTATE.fields_by_name['oper_status'].enum_type = _INTERFACESTATE_OPERSTATUSTYPE
_INTERFACESTATE_ADMINSTATUSTYPE.containing_type = _INTERFACESTATE
_INTERFACESTATE_OPERSTATUSTYPE.containing_type = _INTERFACESTATE
DESCRIPTOR.message_types_by_name['Interfaces'] = _INTERFACES
DESCRIPTOR.message_types_by_name['Interface'] = _INTERFACE
DESCRIPTOR.message_types_by_name['InterfacesState'] = _INTERFACESSTATE
DESCRIPTOR.message_types_by_name['InterfaceState'] = _INTERFACESTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Interfaces = _reflection.GeneratedProtocolMessageType('Interfaces', (_message.Message,), {
  'DESCRIPTOR' : _INTERFACES,
  '__module__' : 'voltha_protos.ietf_interfaces_pb2'
  # @@protoc_insertion_point(class_scope:ietf.Interfaces)
  })
_sym_db.RegisterMessage(Interfaces)

Interface = _reflection.GeneratedProtocolMessageType('Interface', (_message.Message,), {
  'DESCRIPTOR' : _INTERFACE,
  '__module__' : 'voltha_protos.ietf_interfaces_pb2'
  # @@protoc_insertion_point(class_scope:ietf.Interface)
  })
_sym_db.RegisterMessage(Interface)

InterfacesState = _reflection.GeneratedProtocolMessageType('InterfacesState', (_message.Message,), {
  'DESCRIPTOR' : _INTERFACESSTATE,
  '__module__' : 'voltha_protos.ietf_interfaces_pb2'
  # @@protoc_insertion_point(class_scope:ietf.InterfacesState)
  })
_sym_db.RegisterMessage(InterfacesState)

InterfaceState = _reflection.GeneratedProtocolMessageType('InterfaceState', (_message.Message,), {
  'DESCRIPTOR' : _INTERFACESTATE,
  '__module__' : 'voltha_protos.ietf_interfaces_pb2'
  # @@protoc_insertion_point(class_scope:ietf.InterfaceState)
  })
_sym_db.RegisterMessage(InterfaceState)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
