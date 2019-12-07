# Create your views here.
from django.conf import settings
from rest_framework import viewsets, generics, filters
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.manga_api.models import Manga, MangaPart
from apps.manga_api.permissions import IsAdminUserOrReadOnly
from apps.manga_api.serializers import MangaSerializer, MangaHomePageSerializer


class MangaViewSet(viewsets.ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    search_fields = ['russian_name', 'english_name']
    filter_backends = (filters.SearchFilter,)
    permission_classes = [IsAdminUserOrReadOnly, ]
    lookup_field = 'slug'


class MangaLastAddView(APIView):
    """
    GET - Отдает последние добавленные части манги
    """
    permission_classes = [AllowAny, ]

    def get(self, request):
        last_add_part = MangaPart.objects.order_by('-create_time')[:10]
        manga_set = []
        for part in last_add_part:
            photo_url = request.build_absolute_uri(part.manga.poster.url)
            response = {
                'date': part.create_time.strftime("%d-%m-%Y"),
                'created_by': part.created_by.nickname,
                'description': part.manga.descriptions,
                'poster': photo_url,
                'volume': part.volume,
                'part': part.part,
                'rating': part.manga.rating,
                'english_name': part.manga.english_name,
                'slug': part.manga.slug,
            }
            manga_set.append(response)
        return Response(manga_set)


class MangaPromotedView(generics.ListAPIView):
    serializer_class = MangaHomePageSerializer
    permission_classes = [AllowAny, ]
    queryset = Manga.objects.filter(is_promoted=True)[:10]
