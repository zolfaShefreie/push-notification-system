# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from proto import account_pb2 as proto_dot_account__pb2


class WebServerUserControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterWebServer = channel.unary_unary(
                '/account.WebServerUserController/RegisterWebServer',
                request_serializer=proto_dot_account__pb2.WebServer.SerializeToString,
                response_deserializer=proto_dot_account__pb2.WebServer.FromString,
                )
        self.DeleteWebServer = channel.unary_unary(
                '/account.WebServerUserController/DeleteWebServer',
                request_serializer=proto_dot_account__pb2.WebServer.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.AddUser = channel.unary_unary(
                '/account.WebServerUserController/AddUser',
                request_serializer=proto_dot_account__pb2.UserRequest.SerializeToString,
                response_deserializer=proto_dot_account__pb2.User.FromString,
                )
        self.RetrieveUser = channel.unary_unary(
                '/account.WebServerUserController/RetrieveUser',
                request_serializer=proto_dot_account__pb2.UserRetrieveRequest.SerializeToString,
                response_deserializer=proto_dot_account__pb2.User.FromString,
                )
        self.DestroyUser = channel.unary_unary(
                '/account.WebServerUserController/DestroyUser',
                request_serializer=proto_dot_account__pb2.UserRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class WebServerUserControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegisterWebServer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteWebServer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RetrieveUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DestroyUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WebServerUserControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterWebServer': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterWebServer,
                    request_deserializer=proto_dot_account__pb2.WebServer.FromString,
                    response_serializer=proto_dot_account__pb2.WebServer.SerializeToString,
            ),
            'DeleteWebServer': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteWebServer,
                    request_deserializer=proto_dot_account__pb2.WebServer.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'AddUser': grpc.unary_unary_rpc_method_handler(
                    servicer.AddUser,
                    request_deserializer=proto_dot_account__pb2.UserRequest.FromString,
                    response_serializer=proto_dot_account__pb2.User.SerializeToString,
            ),
            'RetrieveUser': grpc.unary_unary_rpc_method_handler(
                    servicer.RetrieveUser,
                    request_deserializer=proto_dot_account__pb2.UserRetrieveRequest.FromString,
                    response_serializer=proto_dot_account__pb2.User.SerializeToString,
            ),
            'DestroyUser': grpc.unary_unary_rpc_method_handler(
                    servicer.DestroyUser,
                    request_deserializer=proto_dot_account__pb2.UserRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'account.WebServerUserController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class WebServerUserController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterWebServer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.WebServerUserController/RegisterWebServer',
            proto_dot_account__pb2.WebServer.SerializeToString,
            proto_dot_account__pb2.WebServer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteWebServer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.WebServerUserController/DeleteWebServer',
            proto_dot_account__pb2.WebServer.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.WebServerUserController/AddUser',
            proto_dot_account__pb2.UserRequest.SerializeToString,
            proto_dot_account__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RetrieveUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.WebServerUserController/RetrieveUser',
            proto_dot_account__pb2.UserRetrieveRequest.SerializeToString,
            proto_dot_account__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DestroyUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.WebServerUserController/DestroyUser',
            proto_dot_account__pb2.UserRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)