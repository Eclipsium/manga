# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets

from apps.custom_user.permissions import IsCurrentUserOrReadOnly
from apps.custom_user.serializers import UserMeSerializer, UserDetailSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsCurrentUserOrReadOnly, ]
    lookup_field = 'nickname'


class UserListProfileView(generics.ListAPIView):
    serializer_class = UserMeSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id)


