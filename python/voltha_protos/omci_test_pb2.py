# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: voltha_protos/omci_test.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='voltha_protos/omci_test.proto',
  package='omci',
  syntax='proto3',
  serialized_options=b'\n\030org.opencord.voltha.omciZ,github.com/opencord/voltha-protos/v5/go/omci',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1dvoltha_protos/omci_test.proto\x12\x04omci\"+\n\x0fOmciTestRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\"u\n\x0cTestResponse\x12\x35\n\x06result\x18\x01 \x01(\x0e\x32%.omci.TestResponse.TestResponseResult\".\n\x12TestResponseResult\x12\x0b\n\x07SUCCESS\x10\x00\x12\x0b\n\x07\x46\x41ILURE\x10\x01\x42H\n\x18org.opencord.voltha.omciZ,github.com/opencord/voltha-protos/v5/go/omcib\x06proto3'
)



_TESTRESPONSE_TESTRESPONSERESULT = _descriptor.EnumDescriptor(
  name='TestResponseResult',
  full_name='omci.TestResponse.TestResponseResult',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FAILURE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=155,
  serialized_end=201,
)
_sym_db.RegisterEnumDescriptor(_TESTRESPONSE_TESTRESPONSERESULT)


_OMCITESTREQUEST = _descriptor.Descriptor(
  name='OmciTestRequest',
  full_name='omci.OmciTestRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='omci.OmciTestRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='omci.OmciTestRequest.uuid', index=1,
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
  serialized_start=39,
  serialized_end=82,
)


_TESTRESPONSE = _descriptor.Descriptor(
  name='TestResponse',
  full_name='omci.TestResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='omci.TestResponse.result', index=0,
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
    _TESTRESPONSE_TESTRESPONSERESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=201,
)

_TESTRESPONSE.fields_by_name['result'].enum_type = _TESTRESPONSE_TESTRESPONSERESULT
_TESTRESPONSE_TESTRESPONSERESULT.containing_type = _TESTRESPONSE
DESCRIPTOR.message_types_by_name['OmciTestRequest'] = _OMCITESTREQUEST
DESCRIPTOR.message_types_by_name['TestResponse'] = _TESTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OmciTestRequest = _reflection.GeneratedProtocolMessageType('OmciTestRequest', (_message.Message,), {
  'DESCRIPTOR' : _OMCITESTREQUEST,
  '__module__' : 'voltha_protos.omci_test_pb2'
  # @@protoc_insertion_point(class_scope:omci.OmciTestRequest)
  })
_sym_db.RegisterMessage(OmciTestRequest)

TestResponse = _reflection.GeneratedProtocolMessageType('TestResponse', (_message.Message,), {
  'DESCRIPTOR' : _TESTRESPONSE,
  '__module__' : 'voltha_protos.omci_test_pb2'
  # @@protoc_insertion_point(class_scope:omci.TestResponse)
  })
_sym_db.RegisterMessage(TestResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)