from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from apps.manga_api.models import Manga

User = get_user_model()


def get_sentinel_user():
    return get_user_model().objects.get_or_create(nickname='deleted')[0]


class Comments(models.Model):
    created_by = models.ForeignKey(User, verbose_name='User', on_delete=models.SET(get_sentinel_user))
    create_time = models.DateTimeField('Create date', auto_now_add=True)
    manga = models.ForeignKey(Manga, verbose_name='Manga', on_delete=models.CASCADE)
    comment_text = models.TextField('Comment text', max_length=400)


