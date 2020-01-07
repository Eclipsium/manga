from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from apps.manga_api.models import Manga

User = get_user_model()


class Vote(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    vote_time = models.DateTimeField('Vote date', auto_now_add=True)
    manga = models.ForeignKey(Manga, verbose_name='Manga', on_delete=models.CASCADE)
    vote_int = models.IntegerField('Vote rating')

    class Meta:
        verbose_name = 'Vote'
        verbose_name_plural = 'Votes'
        unique_together = ('user', 'manga')
