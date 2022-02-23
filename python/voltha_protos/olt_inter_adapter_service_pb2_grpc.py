# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from voltha_protos import common_pb2 as voltha__protos_dot_common__pb2
from voltha_protos import health_pb2 as voltha__protos_dot_health__pb2
from voltha_protos import inter_adapter_pb2 as voltha__protos_dot_inter__adapter__pb2


class OltInterAdapterServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetHealthStatus = channel.unary_unary(
                '/olt_inter_adapter_service.OltInterAdapterService/GetHealthStatus',
                request_serializer=voltha__protos_dot_common__pb2.Connection.SerializeToString,
                response_deserializer=voltha__protos_dot_health__pb2.HealthStatus.FromString,
                )
        self.ProxyOmciRequest = channel.unary_unary(
                '/olt_inter_adapter_service.OltInterAdapterService/ProxyOmciRequest',
                request_serializer=voltha__protos_dot_inter__adapter__pb2.OmciMessage.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetTechProfileInstance = channel.unary_unary(
                '/olt_inter_adapter_service.OltInterAdapterService/GetTechProfileInstance',
                request_serializer=voltha__protos_dot_inter__adapter__pb2.TechProfileInstanceRequestMessage.SerializeToString,
                response_deserializer=voltha__protos_dot_inter__adapter__pb2.TechProfileDownloadMessage.FromString,
                )


class OltInterAdapterServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetHealthStatus(self, request, context):
        """GetHealthStatus is used by an OltInterAdapterService client to verify connectivity
        to the gRPC server hosting the OltInterAdapterService service
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ProxyOmciRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTechProfileInstance(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OltInterAdapterServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetHealthStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetHealthStatus,
                    request_deserializer=voltha__protos_dot_common__pb2.Connection.FromString,
                    response_serializer=voltha__protos_dot_health__pb2.HealthStatus.SerializeToString,
            ),
            'ProxyOmciRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.ProxyOmciRequest,
                    request_deserializer=voltha__protos_dot_inter__adapter__pb2.OmciMessage.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetTechProfileInstance': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTechProfileInstance,
                    request_deserializer=voltha__protos_dot_inter__adapter__pb2.TechProfileInstanceRequestMessage.FromString,
                    response_serializer=voltha__protos_dot_inter__adapter__pb2.TechProfileDownloadMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'olt_inter_adapter_service.OltInterAdapterService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OltInterAdapterService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetHealthStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/olt_inter_adapter_service.OltInterAdapterService/GetHealthStatus',
            voltha__protos_dot_common__pb2.Connection.SerializeToString,
            voltha__protos_dot_health__pb2.HealthStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ProxyOmciRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/olt_inter_adapter_service.OltInterAdapterService/ProxyOmciRequest',
            voltha__protos_dot_inter__adapter__pb2.OmciMessage.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTechProfileInstance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/olt_inter_adapter_service.OltInterAdapterService/GetTechProfileInstance',
            voltha__protos_dot_inter__adapter__pb2.TechProfileInstanceRequestMessage.SerializeToString,
            voltha__protos_dot_inter__adapter__pb2.TechProfileDownloadMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
