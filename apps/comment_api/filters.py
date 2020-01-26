import django_filters

from apps.comment_api.models import Comments


class MangaCommentsFilter(django_filters.FilterSet):
    manga = django_filters.CharFilter(field_name='manga')
    created_by = django_filters.CharFilter(field_name='created_by__nickname')

    class Meta:
        model = Comments
        fields = ('manga', 'created_by')

