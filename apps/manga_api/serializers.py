from rest_framework import serializers

from apps.manga_api.models import *


class MangaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manga
        fields = '__all__'


class MangaHomePageSerializer(serializers.ModelSerializer):
    """
    Сериализатор для главной страницы
    """
    # def get_foo(self, obj):

    class Meta:
        model = Manga
        fields = ('english_name', 'slug', 'poster', 'rating', 'descriptions',)
