from django.contrib.auth import get_user_model
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField

User = get_user_model()


class UserMeSerializer(serializers.ModelSerializer):
    is_superuser = serializers.ReadOnlyField()
    avatar = HyperlinkedSorlImageField('100')

    class Meta:
        model = User
        fields = ("id", "email", "nickname", "avatar", 'is_superuser')


class UserDetailSerializer(serializers.ModelSerializer):
    avatar = HyperlinkedSorlImageField('100')

    class Meta:
        model = User
        fields = ("id", "email", "nickname", "avatar")


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ("id", "email", "nickname", "password")
