from django_grpc_framework import services
import grpc

from .models import User, WebServer
from .serializers import WebServerSrializer, UserSerializer
from .utility import login
from proto import account_pb2_grpc, account_pb2


class WebServerUserService(services.Service):

    def RegisterWebServer(self, request, context):
        serializer = WebServerSrializer(message=request)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return serializer.message
    
    def perform_create(self, serializer):
        serializer.save()
    
    def DeleteWebServer(self, request, context):
        web = login(request.login.name, request.login.password)
        if web is None:
            self.context.abort(grpc.StatusCode.PERMISSION_DENIED)
        try:
            instance = WebServer.objects.get(name=request.WebServer.name)
        except:
            self.context.abort(grpc.StatusCode.NOT_FOUND, 'Webserver:%s not found!' % request.WebServer.name)

        if web != instance:
            self.context.abort(grpc.StatusCode.PERMISSION_DENIED)

        self.perform_destroy(instance)
        return empty_pb2.Empty()

    def perform_destroy(self, instance):
        instance.delete()

    def AddUser(self, request, context):
        web = login(request.login.name, request.login.password)
        if web is None:
            self.context.abort(grpc.StatusCode.PERMISSION_DENIED)
        if web.id != request.user.webserver:
            self.context.abort(grpc.StatusCode.PERMISSION_DENIED)

        serializer = UserSerializer(message=request.user)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return serializer.message

    def RetrieveUser(self, request, context):
        web = login(request.login.name, request.login.password)
        if web is None:
            self.context.abort(grpc.StatusCode.PERMISSION_DENIED)
        try:
            user = User.objects.get(pk=request.user.id)
        except:
            self.context.abort(grpc.StatusCode.NOT_FOUND,
                               'user:%s not found!' % request.user.id)

        if user.webserver.id != web.id:
            self.context.abort(grpc.StatusCode.PERMISSION_DENIED)

        serializer = UserSerializer(user)
        return serializer.message

    def DestroyUser(self, request, context):
        web = login(request.login.name, request.login.password)
        if web is None:
            self.context.abort(grpc.StatusCode.PERMISSION_DENIED)

        try:
            user = User.objects.get(pk=request.user.id)
        except:
            self.context.abort(grpc.StatusCode.NOT_FOUND,
                               'user:%s not found!' % request.user.id)

        if user.webserver.id != web.id:
            self.context.abort(grpc.StatusCode.PERMISSION_DENIED)

        self.perform_destroy(user)
        return empty_pb2.Empty()

    
