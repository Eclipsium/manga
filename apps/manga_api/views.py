# Create your views here.
from django.conf import settings
from rest_framework import viewsets, generics, filters
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.manga_api.models import Manga, MangaVolume, MangaArtist
from apps.manga_api.permissions import IsAdminUserOrReadOnly
from apps.manga_api.serializers import MangaSerializer, MangaHomePageSerializer, MangaListSerializer, \
    MangaArtistSerializer


class MangaArtistViewSet(viewsets.ModelViewSet):
    queryset = MangaArtist.objects.all()
    serializer_class = MangaArtistSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    lookup_field = 'slug'


class MangaViewSet(viewsets.ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    search_fields = ['japan_name', 'english_name']
    filter_backends = (filters.SearchFilter,)
    permission_classes = [IsAdminUserOrReadOnly, ]
    lookup_field = 'slug'


class MangaListView(generics.ListAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaListSerializer
    permission_classes = [AllowAny,]
    search_fields = ['japan_name', 'english_name']
    filter_backends = (filters.SearchFilter,)


class MangaLastAddView(APIView):
    """
    GET - Отдает последние добавленные части манги
    """
    permission_classes = [AllowAny, ]

    def get(self, request):
        last_add_volume = MangaVolume.objects.order_by('-create_time')[:10]
        manga_set = []
        for volume in last_add_volume:
            photo_url = request.build_absolute_uri(volume.manga.poster.url)
            response = {
                'date': volume.create_time.strftime("%d-%m-%Y"),
                'japan_name': volume.manga.japan_name,
                'description': volume.manga.descriptions,
                'poster': photo_url,
                'volume': volume.volume,
                'rating': volume.manga.rating,
                'english_name': volume.manga.english_name,
                'slug': volume.manga.slug,
            }
            manga_set.append(response)
        return Response(manga_set)


class MangaMainPageView(APIView):
    """
    GET - Отдает информацию о манге и ее части
    """
    permission_classes = [AllowAny, ]

    def get(self, request, *args, **kwargs):
        manga = Manga.objects.get(slug=kwargs['slug'])
        volumes = manga.mangavolume_set.all()
        manga_set = []
        for volume in volumes:
            response = {
                'date': volume.create_time.strftime("%d-%m-%Y"),
                'volume': volume.volume,
                'created_by': volume.created_by.nickname,
                'image_count': volume.mangaimage_set.count()
            }
            manga_set.append(response)
        return Response(manga_set)


class MangaPromotedView(generics.ListAPIView):
    serializer_class = MangaHomePageSerializer
    permission_classes = [AllowAny, ]
    queryset = Manga.objects.filter(is_promoted=True)[:10]
