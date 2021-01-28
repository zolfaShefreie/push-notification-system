from django_grpc_framework import proto_serializers
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import User, WebServer
from proto import account_pb2


# class LoginSerializer(proto_serializerss.ModelProtoSerializer):
#     class Meta:
#         model = WebServer
#         proto_class = account_pb2.Login
#         fields = ['name', 'password']

#     def validate_password(self, value):
#         pass


class WebServerSrializer(proto_serializers.ModelProtoSerializer):

    class Meta:
        model = WebServer
        proto_class = account_pb2.WebServer
        fields = ["id", "name", "email", "password", "URLAddress"]

    def data_to_message(self, data):
        try:
            data['password'] = ""
        except:
            pass
        return super().data_to_message(data)

    def create(self, validated_data):
        web = super().create(validated_data)
        password = validated_data['password']
        web.set_password(password)
        web.save()
        return web


class UserSerializer(proto_serializers.ModelProtoSerializer):
    token = serializers.SerializerMethodField('get_token')

    class Meta:
        model = User
        proto_class = account_pb2.User
        fields = ['id', 'webserver', 'token']

    def get_token(self, obj):
        token, create = Token.objects.get_or_create(user=obj)
        return token.key

