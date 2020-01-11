import django_filters

from apps.manga_api.models import Manga


class PromoteAndArtistsFilter(django_filters.FilterSet):
    artists = django_filters.CharFilter(lookup_expr='icontains')
    is_promoted = django_filters.BooleanFilter(field_name='is_promoted')
    create_by_user = django_filters.CharFilter(field_name='create_by_user__nickname')

    class Meta:
        model = Manga
        fields = ('artists', 'is_promoted', 'create_by_user')
