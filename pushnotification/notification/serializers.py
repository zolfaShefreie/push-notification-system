from rest_framework import serializers
from proto import notification_pb2
from .models import Notification, NotificationType
from django_grpc_framework import proto_serializers


class NotificationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationType
        fields = "__all__"


class NotificationSerializer(serializers.ModelSerializer):
    notification_type = NotificationTypeSerializer()

    class Meta:
        model = Notification
        fields = "__all__"


class NotificationProtoSerializer(proto_serializers.ModelProtoSerializer):

    class Meta:
        model = Notification
        proto_class = notification_pb2.Notification
        fields = ["id", "text", "created_date", "sender_name", "icon_URL", "receiver", "notification_type"]

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance


class NotificationTypeProtoSerializer(proto_serializers.ModelProtoSerializer):

    class Meta:
        model = NotificationType
        proto_class = notification_pb2.NotificationType
        fields = ["id", "name", "icon", "priority", "webserver"]

