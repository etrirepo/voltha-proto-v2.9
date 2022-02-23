# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: voltha_protos/core_services.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from voltha_protos import core_adapter_pb2 as voltha__protos_dot_core__adapter__pb2
from voltha_protos import common_pb2 as voltha__protos_dot_common__pb2
from voltha_protos import device_pb2 as voltha__protos_dot_device__pb2
from voltha_protos import health_pb2 as voltha__protos_dot_health__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='voltha_protos/core_services.proto',
  package='core_service',
  syntax='proto3',
  serialized_options=b'\n org.opencord.voltha.core_serviceB\021VolthaCoreServiceZ4github.com/opencord/voltha-protos/v5/go/core_service',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!voltha_protos/core_services.proto\x12\x0c\x63ore_service\x1a\x1bgoogle/protobuf/empty.proto\x1a voltha_protos/core_adapter.proto\x1a\x1avoltha_protos/common.proto\x1a\x1avoltha_protos/device.proto\x1a\x1avoltha_protos/health.proto2\xf9\x0b\n\x0b\x43oreService\x12;\n\x0fGetHealthStatus\x12\x12.common.Connection\x1a\x14.health.HealthStatus\x12L\n\x0fRegisterAdapter\x12!.core_adapter.AdapterRegistration\x1a\x16.google.protobuf.Empty\x12\x36\n\x0c\x44\x65viceUpdate\x12\x0e.device.Device\x1a\x16.google.protobuf.Empty\x12\x33\n\x0bPortCreated\x12\x0c.device.Port\x1a\x16.google.protobuf.Empty\x12I\n\x10PortsStateUpdate\x12\x1d.core_adapter.PortStateFilter\x1a\x16.google.protobuf.Empty\x12\x34\n\x0e\x44\x65leteAllPorts\x12\n.common.ID\x1a\x16.google.protobuf.Empty\x12\x37\n\rGetDevicePort\x12\x18.core_adapter.PortFilter\x1a\x0c.device.Port\x12,\n\x0fListDevicePorts\x12\n.common.ID\x1a\r.device.Ports\x12L\n\x11\x44\x65viceStateUpdate\x12\x1f.core_adapter.DeviceStateFilter\x1a\x16.google.protobuf.Empty\x12\x41\n\x14\x44\x65vicePMConfigUpdate\x12\x11.device.PmConfigs\x1a\x16.google.protobuf.Empty\x12\x44\n\x13\x43hildDeviceDetected\x12\x1d.core_adapter.DeviceDiscovery\x1a\x0e.device.Device\x12\x36\n\x10\x43hildDevicesLost\x12\n.common.ID\x1a\x16.google.protobuf.Empty\x12:\n\x14\x43hildDevicesDetected\x12\n.common.ID\x1a\x16.google.protobuf.Empty\x12\'\n\tGetDevice\x12\n.common.ID\x1a\x0e.device.Device\x12\x41\n\x0eGetChildDevice\x12\x1f.core_adapter.ChildDeviceFilter\x1a\x0e.device.Device\x12.\n\x0fGetChildDevices\x12\n.common.ID\x1a\x0f.device.Devices\x12>\n\x0cSendPacketIn\x12\x16.core_adapter.PacketIn\x1a\x16.google.protobuf.Empty\x12H\n\x12\x44\x65viceReasonUpdate\x12\x1a.core_adapter.DeviceReason\x1a\x16.google.protobuf.Empty\x12\x42\n\x0fPortStateUpdate\x12\x17.core_adapter.PortState\x1a\x16.google.protobuf.Empty\x12;\n\x15ReconcileChildDevices\x12\n.common.ID\x1a\x16.google.protobuf.Empty\x12M\n\x1eGetChildDeviceWithProxyAddress\x12\x1b.device.Device.ProxyAddress\x1a\x0e.device.Device\x12\x33\n\x08GetPorts\x12\x18.core_adapter.PortFilter\x1a\r.device.Ports\x12N\n\x13\x43hildrenStateUpdate\x12\x1f.core_adapter.DeviceStateFilter\x1a\x16.google.protobuf.Empty\x12\x44\n\x13UpdateImageDownload\x12\x15.device.ImageDownload\x1a\x16.google.protobuf.EmptyBk\n org.opencord.voltha.core_serviceB\x11VolthaCoreServiceZ4github.com/opencord/voltha-protos/v5/go/core_serviceb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,voltha__protos_dot_core__adapter__pb2.DESCRIPTOR,voltha__protos_dot_common__pb2.DESCRIPTOR,voltha__protos_dot_device__pb2.DESCRIPTOR,voltha__protos_dot_health__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_CORESERVICE = _descriptor.ServiceDescriptor(
  name='CoreService',
  full_name='core_service.CoreService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=199,
  serialized_end=1728,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetHealthStatus',
    full_name='core_service.CoreService.GetHealthStatus',
    index=0,
    containing_service=None,
    input_type=voltha__protos_dot_common__pb2._CONNECTION,
    output_type=voltha__protos_dot_health__pb2._HEALTHSTATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RegisterAdapter',
    full_name='core_service.CoreService.RegisterAdapter',
    index=1,
    containing_service=None,
    input_type=voltha__protos_dot_core__adapter__pb2._ADAPTERREGISTRATION,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeviceUpdate',
    full_name='core_service.CoreService.DeviceUpdate',
    index=2,
    containing_service=None,
    input_type=voltha__protos_dot_device__pb2._DEVICE,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PortCreated',
    full_name='core_service.CoreService.PortCreated',
    index=3,
    containing_service=None,
    input_type=voltha__protos_dot_device__pb2._PORT,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PortsStateUpdate',
    full_name='core_service.CoreService.PortsStateUpdate',
    index=4,
    containing_service=None,
    input_type=voltha__protos_dot_core__adapter__pb2._PORTSTATEFILTER,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteAllPorts',
    full_name='core_service.CoreService.DeleteAllPorts',
    index=5,
    containing_service=None,
    input_type=voltha__protos_dot_common__pb2._ID,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetDevicePort',
    full_name='core_service.CoreService.GetDevicePort',
    index=6,
    containing_service=None,
    input_type=voltha__protos_dot_core__adapter__pb2._PORTFILTER,
    output_type=voltha__protos_dot_device__pb2._PORT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListDevicePorts',
    full_name='core_service.CoreService.ListDevicePorts',
    index=7,
    containing_service=None,
    input_type=voltha__protos_dot_common__pb2._ID,
    output_type=voltha__protos_dot_device__pb2._PORTS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeviceStateUpdate',
    full_name='core_service.CoreService.DeviceStateUpdate',
    index=8,
    containing_service=None,
    input_type=voltha__protos_dot_core__adapter__pb2._DEVICESTATEFILTER,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DevicePMConfigUpdate',
    full_name='core_service.CoreService.DevicePMConfigUpdate',
    index=9,
    containing_service=None,
    input_type=voltha__protos_dot_device__pb2._PMCONFIGS,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ChildDeviceDetected',
    full_name='core_service.CoreService.ChildDeviceDetected',
    index=10,
    containing_service=None,
    input_type=voltha__protos_dot_core__adapter__pb2._DEVICEDISCOVERY,
    output_type=voltha__protos_dot_device__pb2._DEVICE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ChildDevicesLost',
    full_name='core_service.CoreService.ChildDevicesLost',
    index=11,
    containing_service=None,
    input_type=voltha__protos_dot_common__pb2._ID,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ChildDevicesDetected',
    full_name='core_service.CoreService.ChildDevicesDetected',
    index=12,
    containing_service=None,
    input_type=voltha__protos_dot_common__pb2._ID,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetDevice',
    full_name='core_service.CoreService.GetDevice',
    index=13,
    containing_service=None,
    input_type=voltha__protos_dot_common__pb2._ID,
    output_type=voltha__protos_dot_device__pb2._DEVICE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetChildDevice',
    full_name='core_service.CoreService.GetChildDevice',
    index=14,
    containing_service=None,
    input_type=voltha__protos_dot_core__adapter__pb2._CHILDDEVICEFILTER,
    output_type=voltha__protos_dot_device__pb2._DEVICE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetChildDevices',
    full_name='core_service.CoreService.GetChildDevices',
    index=15,
    containing_service=None,
    input_type=voltha__protos_dot_common__pb2._ID,
    output_type=voltha__protos_dot_device__pb2._DEVICES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SendPacketIn',
    full_name='core_service.CoreService.SendPacketIn',
    index=16,
    containing_service=None,
    input_type=voltha__protos_dot_core__adapter__pb2._PACKETIN,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeviceReasonUpdate',
    full_name='core_service.CoreService.DeviceReasonUpdate',
    index=17,
    containing_service=None,
    input_type=voltha__protos_dot_core__adapter__pb2._DEVICEREASON,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PortStateUpdate',
    full_name='core_service.CoreService.PortStateUpdate',
    index=18,
    containing_service=None,
    input_type=voltha__protos_dot_core__adapter__pb2._PORTSTATE,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReconcileChildDevices',
    full_name='core_service.CoreService.ReconcileChildDevices',
    index=19,
    containing_service=None,
    input_type=voltha__protos_dot_common__pb2._ID,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetChildDeviceWithProxyAddress',
    full_name='core_service.CoreService.GetChildDeviceWithProxyAddress',
    index=20,
    containing_service=None,
    input_type=voltha__protos_dot_device__pb2._DEVICE_PROXYADDRESS,
    output_type=voltha__protos_dot_device__pb2._DEVICE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetPorts',
    full_name='core_service.CoreService.GetPorts',
    index=21,
    containing_service=None,
    input_type=voltha__protos_dot_core__adapter__pb2._PORTFILTER,
    output_type=voltha__protos_dot_device__pb2._PORTS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ChildrenStateUpdate',
    full_name='core_service.CoreService.ChildrenStateUpdate',
    index=22,
    containing_service=None,
    input_type=voltha__protos_dot_core__adapter__pb2._DEVICESTATEFILTER,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateImageDownload',
    full_name='core_service.CoreService.UpdateImageDownload',
    index=23,
    containing_service=None,
    input_type=voltha__protos_dot_device__pb2._IMAGEDOWNLOAD,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CORESERVICE)

DESCRIPTOR.services_by_name['CoreService'] = _CORESERVICE

# @@protoc_insertion_point(module_scope)