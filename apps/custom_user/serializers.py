from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "full_name", "nickname", "is_staff", "avatar")


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "full_name", "nickname", "avatar")

