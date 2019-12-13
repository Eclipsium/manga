import django_filters

from apps.manga_api.models import Manga


class MangaFilter(django_filters.FilterSet):
    class Meta:
        model = Manga
        fields = ['rating', 'is_promoted']
