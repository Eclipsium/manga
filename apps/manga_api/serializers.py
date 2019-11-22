from rest_framework import serializers

from apps.manga_api.models import Manga


class MangaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manga
        fields = ('id', 'russian_name', 'english_name', 'slug', 'categories', 'author',
                  'drawer', 'year', 'translation', 'poster', 'rating')



