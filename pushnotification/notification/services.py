from django_grpc_framework import services
import grpc

from .models import Notification, NotificationType
from .serializers import NotificationSerializer, NotificationTypeSerializer
from .utility import is_owner_user, is_owner_notif_type
from account.models import User, WebServer
from account.utility import login
from google.protobuf import empty_pb2


class NotificaionServicer(services.Service):

    def CreateNotification(self, request, context):
        web = login(request.login.name, request.login.password)
        if web is None:
            self.context.abort(grpc.StatusCode.PERMISSION_DENIED, "LOGIN FAILED")

        if not is_owner_user(web, request.receiver) or not is_owner_notif_type(web, request.notification_type):
            self.context.abort(grpc.StatusCode.PERMISSION_DENIED, "PERMISSION_DENIED")
        serializer = NotificationSerializer(message=request.notification)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return serializer.message
        
    def perform_create(self, serializer):
        serializer.save()

    def CreateNotificationType(self, request, context):
        web = login(request.login.name, request.login.password)
        if web is None:
            self.context.abort(grpc.StatusCode.PERMISSION_DENIED, "LOGIN FAILED")

        if web.id != request.notification_type.webserver:
            self.context.abort(grpc.StatusCode.PERMISSION_DENIED, "PERMISSION_DENIED")
        serializer = NotificationTypeSerializer(message=request.notification_type)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return serializer.message      

    def UpdateNotification(self, request, context):
        web = login(request.login.name, request.login.password)
        if web is None:
            self.context.abort(grpc.StatusCode.PERMISSION_DENIED, "LOGIN FAILED")

        serializer = NotificationSerializer(message=request.notification, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message       

    def DestroyNotification(self, request, context):
        web = login(request.login.name, request.login.password)
        if web is None:
            self.context.abort(grpc.StatusCode.PERMISSION_DENIED, "LOGIN FAILED")
        
        try:
            notif = Notification.objects.get(request.notification.id)
        except:
            self.context.abort(grpc.StatusCode.NOT_FOUND, 'notification:%s not found!' % request.notification.id)
        
        if not is_owner_user(web, notif.receiver.id):
            self.context.abort(grpc.StatusCode.PERMISSION_DENIED, "PERMISSION_DENIED")
        
        self.perform_destroy(notif)
        return empty_pb2.Empty()
    
    def perform_destroy(self, instance):
        instance.delete()
    
    