from django.db import models
from account.models import User, WebServer
# Create your models here.


class NotificationType(models.Model):
    name = models.CharField(max_length=100)
    icon = models.URLField()
    priority = models.PositiveIntegerField(default=10)
    webserver = models.ForeignKey('WebServer', on_delete=models.CASCADE)


class Notification(models.Model):
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, blank=False)
    sender_name = models.CharField(max_length=100)
    icon_URL = models.URLField()
    receiver_name = models.ForeignKey('User', models.CASCADE)
    notification_type = models.ForeignKey('NotificationType', models.CASCADE)

    class Meta:
        index_together = [
            ["receiver_name_id"],
        ]
