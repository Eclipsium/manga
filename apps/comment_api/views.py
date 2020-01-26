# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.comment_api.filters import MangaCommentsFilter
from apps.comment_api.models import Comments
from apps.comment_api.permissions import IsCreatorOrAdminOrReadOnly
from apps.comment_api.serializers import CommentPostSerializer, CommentGetSerializer


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsCreatorOrAdminOrReadOnly, IsAuthenticatedOrReadOnly)
    queryset = Comments.objects.filter()
    filterset_class = MangaCommentsFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return CommentGetSerializer
        else:
            return CommentPostSerializer
