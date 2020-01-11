from django.contrib.auth import get_user_model
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

User = get_user_model()


class UserMeSerializer(serializers.ModelSerializer):
    is_superuser = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ("id", "email", "nickname", "avatar", 'is_superuser')


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "nickname", "avatar")


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ("id", "email", "nickname", "password")
