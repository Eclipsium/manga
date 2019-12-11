from rest_framework import serializers

from apps.manga_api.models import *


class MangaArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = MangaArtist
        fields = ['name', 'slug']


class MangaSerializer(serializers.ModelSerializer):
    artists = MangaArtistSerializer(many=True)

    class Meta:
        model = Manga
        fields = [
            'japan_name', 'english_name', 'descriptions', 'slug', 'categories', 'poster', 'rating',
            'is_promoted', 'artists'
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
    Сериализатор для поиска манги
    """

    class Meta:
        model = Manga
        fields = ('english_name',)
