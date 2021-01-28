from django_grpc_framework import proto_serializers
from rest_framework import serializers

from .models import Notification, NotificationType
from proto import notification_pb2


class NotificationSerializer(proto_serializers.ModelProtoSerializer):

    class Meta:
        model = Notification
        proto_class = notification_pb2.Notification
        fields = ["id", "text", "created_date", "sender_name", "icon_URL", "receiver", "notification_type"]


class NotificationTypeSerializer(proto_serializers.ModelProtoSerializer):

    class Meta:
        model = NotificationType
        proto_class = notification_pb2.NotificationType
        fields = ["id", "name", "icon", "priority", "webserver"]