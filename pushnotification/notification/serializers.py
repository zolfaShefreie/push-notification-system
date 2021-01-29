from rest_framework import serializers
from .models import Notification, NotificationType


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"
