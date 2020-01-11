# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, filters, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.manga_api.models import Manga, MangaVolume, MangaArchive, MangaImage
from apps.manga_api.permissions import IsAdminUserOrReadOnly
from apps.manga_api.serializers import MangaSerializer, MangaHomePageSerializer, MangaListSerializer, \
    MangaArchiveSerializer, MangaImageViewSerializer, MangaVolumeSerializer
from .filters import PromoteAndArtistsFilter
from .tasks import parse_task_data


class MangaViewSet(viewsets.ModelViewSet):
    queryset = Manga.objects.filter()
    serializer_class = MangaSerializer
    search_fields = ['japan_name', 'english_name']
    filter_backends = (filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter)
    permission_classes = [IsAdminUserOrReadOnly, ]
    lookup_field = 'slug'
    ordering_fields = ['rating', 'is_promoted']
    filterset_class = PromoteAndArtistsFilter
    # filterset_fields = ('is_promoted',)


class MangaListView(generics.ListAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaListSerializer
    permission_classes = [AllowAny, ]
    search_fields = ['japan_name', 'english_name']
    filter_backends = (filters.SearchFilter,)


class MangaLastAddView(APIView):
    """
    GET - Отдает последние добавленные части манги
    """
    permission_classes = [AllowAny, ]

    def get(self, request):
        last_add_volume = MangaVolume.objects.order_by('create_time')
        manga_set = []
        for volume in last_add_volume:
            photo_url = request.build_absolute_uri(volume.manga.poster.url)
            response = {
                'date': volume.create_time.strftime("%d-%m-%Y"),
                'japan_name': volume.manga.japan_name,
                'descriptions': volume.manga.descriptions,
                'poster': photo_url,
                'volume': volume.volume,
                'rating': volume.manga.rating,
                'english_name': volume.manga.english_name,
                'slug': volume.manga.slug,
                'is_promoted': volume.manga.is_promoted,
            }
            manga_set.append(response)
        #  generator to make unique dict from response list
        manga_set = list({v['slug']: v for v in manga_set}.values())
        return Response({'results': manga_set})


class MangaVolumeDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAdminUserOrReadOnly,]
    serializer_class = MangaVolumeSerializer

    def destroy(self, request, *args, **kwargs):
        volume_pk = kwargs['pk']
        try:
            volume = MangaVolume.objects.get(pk=volume_pk)
        except ObjectDoesNotExist:
            return Response('error: Volume with id ' + volume_pk + ' not found', status=status.HTTP_404_NOT_FOUND)
        volume.delete()
        return Response('deleted!', status=status.HTTP_200_OK)


class MangaVolumeCreateView(APIView):
    """
    GET - Create new volume for manga
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        manga_slug = kwargs['slug']
        volume_pk = kwargs['pk']

        try:
            manga = Manga.objects.get(slug=manga_slug)
        except ObjectDoesNotExist:
            return Response('error: manga with name ' + kwargs['slug'] + ' not found', status=status.HTTP_404_NOT_FOUND)

        if manga:
            try:
                MangaVolume.objects.create(manga=manga, volume=volume_pk, created_by=request.user)
                return Response('created', status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response('message: Manga volume already created!', status=status.HTTP_400_BAD_REQUEST)


class MangaSearchArtistView(generics.ListAPIView):
    serializer_class = MangaSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        slug = self.kwargs['slug']
        print(slug)
        return Manga.objects.filter(artists=slug)


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
                'id': volume.pk,
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
    queryset = Manga.objects.filter(is_promoted=True)


class MangaArchiveCreateView(generics.CreateAPIView):
    queryset = MangaArchive.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = MangaArchiveSerializer

    def perform_create(self, serializer):
        try:
            manga_volume = MangaVolume.objects.get(manga=self.request.data['manga'], volume=self.request.data['volume'])
            raise ValidationError('Manga volume already exist!')
        except ObjectDoesNotExist:
            instance = serializer.save()
            manga_volume = MangaVolume.objects.create(
                created_by=self.request.user,
                volume=instance.volume,
                manga=instance.manga
            ).pk
            parse_task_data.delay(archive_id=instance.id, manga_volume=manga_volume)


class MangaImageListView(generics.ListAPIView):
    serializer_class = MangaImageViewSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        volume_pk = self.kwargs['pk']
        return MangaImage.objects.filter(volume=volume_pk).order_by('sort_index')
