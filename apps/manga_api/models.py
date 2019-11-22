import os
import uuid

from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

from django.contrib.postgres.fields import ArrayField
from pytils.translit import slugify

from apps.manga_api.categories import MANGA_CATEGORIES

User = get_user_model()


class ChoiceArrayField(ArrayField):
    """
    A field that allows us to store an array of choices.
    Uses Django's Postgres ArrayField
    and a MultipleChoiceField for its formfield.
    """

    def formfield(self, **kwargs):
        defaults = {
            'form_class': forms.MultipleChoiceField,
            'choices': self.base_field.choices,
        }
        defaults.update(kwargs)
        # Skip our parent's formfield implementation completely as we don't
        # care for it.
        # pylint:disable=bad-super-call
        return super(ArrayField, self).formfield(**defaults)


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('posters/', instance.manga_original_name, filename)


# class MangaPerson(models.Model):
#     full_name = models.CharField('Полное имя', max_length=100)
#     slug = models.SlugField('url', unique=True, blank=True)
#
#     def __str__(self):
#         return str(self.full_name)
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.full_name)
#         super(MangaPerson, self).save(*args, **kwargs)
#
#     class Meta:
#         verbose_name = 'Профиль'
#         verbose_name_plural = 'Профили'


class Manga(models.Model):
    russian_name = models.CharField('Название на русском', max_length=100, unique=True)
    english_name = models.CharField('Название на английском', max_length=100, unique=True)
    descriptions = models.TextField('Описание', max_length=500)
    slug = models.SlugField('url', unique=True, blank=True)
    volumes = models.IntegerField('Количество томов')
    categories = ChoiceArrayField(
        models.CharField(choices=MANGA_CATEGORIES, max_length=15, blank=True), blank=True, null=True)
    author = models.CharField('Сценарист', max_length=100)
    drawer = models.CharField('Художник', max_length=100)
    year = models.IntegerField('Год выпуска')
    translation = models.CharField('Переводчик', max_length=100)
    poster = models.ImageField('Обложка', upload_to=get_file_path, blank=True, null=True)
    rating = models.FloatField('Рейтинг', default=0)

    def __str__(self):
        return str(self.russian_name) + ' | ' + str(self.slug)

    class Meta:
        verbose_name = 'Манга'
        verbose_name_plural = 'Манга'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.english_name)
        super(Manga, self).save(*args, **kwargs)


@receiver(post_delete, sender=Manga)
def delete_img_from_media(sender, instance, **kwargs):
    os.remove(os.path.join(settings.MEDIA_ROOT, instance.poster.name))


@receiver(pre_save, sender=Manga)
def delete_file_on_change_extension(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_poster = Manga.objects.get(pk=instance.pk).poster
        except Manga.DoesNotExist:
            return
        else:
            new_poster = instance.poster
            if old_poster and old_poster.url != new_poster.url:
                old_poster.delete(save=False)
