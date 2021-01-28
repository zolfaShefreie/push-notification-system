from django_grpc_framework import proto_serializerss
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


class WebServerSrializer(proto_serializerss.ModelProtoSerializer):

    class Meta:
        model = WebServer
        proto_class = account_pb2.WebServer
        fields = ["id", "name", "password", "URLAddress"]

    # def create(self, validated_data):
    #     pass

    def data_to_message(self, data):
        try:
            data['password'] = ""
        except:
            pass
        return super().data_to_message(data)


class UserSerializer(proto_serializerss.ModelProtoSerializer):
    token = serializers.SerializerMethodField('get_token')

    class Meta:
        model = User
        proto_calss = account_pb2.User
        fields = ['id', 'webserver', 'token']

    def get_token(self, obj):
        token = Token.objects.get_or_create(user=obj)
        return token.key

