from rest_framework import serializers
from rest_framework.fields import ImageField

from apps.manga_api.models import *


class MangaSerializer(serializers.ModelSerializer):
    create_by_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = Manga
        fields = [
            'id', 'english_name', 'descriptions', 'slug', 'poster', 'rating',
            'is_promoted', 'artists', 'create_by_user'
        ]


class MangaHomePageSerializer(serializers.ModelSerializer):
    """
    Сериализатор для главной страницы
    """

    # def get_foo(self, obj):

    class Meta:
        model = Manga
        fields = ('english_name', 'slug', 'poster', 'rating', 'descriptions',)


class MangaListSerializer(serializers.ModelSerializer):
    """
    Serializer for search manga
    """

    class Meta:
        model = Manga
        fields = ('english_name',)


class MangaArchiveSerializer(serializers.ModelSerializer):
    """
    Serializer for archives
    """

    class Meta:
        model = MangaArchive
        fields = '__all__'


class MangaImageViewSerializer(serializers.ModelSerializer):
    """
    Serializer for manga image view page
    """

    class Meta:
        model = MangaImage
        fields = ('sort_index', 'image')


class MangaVolumeSerializer(serializers.ModelSerializer):
    """Serialuzer for volume"""

    class Meta:
        model = MangaVolume
        field = ('id',)
