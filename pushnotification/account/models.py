from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class WebServer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    URLAddress = models.URLField(unique=True)


class User(AbstractBaseUser):
    webserver = models.ForeignKey(WebServer, on_delete=models.CASCADE)
    USERNAME_FIELD = 'id'
    last_login = None
    password = None

    class Meta:
        index_together = [
            ["webserver_id"],
        ]




