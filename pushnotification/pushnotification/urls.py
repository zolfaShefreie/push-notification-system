"""pushnotification URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from account.services import WebServerUserService
from notification.services import NotificaionServicer
from proto import account_pb2_grpc, account_pb2, notification_pb2, notification_pb2_grpc

urlpatterns = [
    path('admin/', admin.site.urls),
]


def grpc_handlers(server):
    account_pb2_grpc.add_WebServerUserControllerServicer_to_server(WebServerUserService.as_servicer(), server)
    notification_pb2_grpc.add_NotificationControllerServicer_to_server(NotificaionServicer.as_servicer(), server)
