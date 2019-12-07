# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework import generics

from apps.custom_user.serializers import UserMeSerializer, UserUpdateSerializer

User = get_user_model()


class UserListProfileView(generics.ListAPIView):
    serializer_class = UserMeSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)


class UserUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = UserUpdateSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)

