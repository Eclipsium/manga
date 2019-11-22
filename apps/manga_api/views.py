# Create your views here.
from rest_framework import viewsets

from apps.manga_api.models import Manga
from apps.manga_api.serializers import MangaSerializer


class MangaViewSet(viewsets.ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    lookup_field = 'slug'


# class MangaPersonViewSet(viewsets.ModelViewSet):
#     queryset = MangaPerson.objects.all()
#     serializer_class = MangaPersonSerializer
#     lookup_field = 'slug'
