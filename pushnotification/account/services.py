from django_grpc_framework import services
import grpc

from .models import User, WebServer
from .serializers import WebServerSrializer
from .utility import login
from proto import account_pb2_grpc, account_pb2


class WebServerService(services.Service):

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
    

class UserService(services.Service):

    def AddUser(self, request, context):
        #login process
        pass
        #check is same login web and 
        #save 
        #take token

    def RetrieveUser(self, request, context):
        pass

    def DestroyUser(self, request, context):
        pass
    
