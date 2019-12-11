import os
import uuid
from datetime import datetime

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


def get_poster_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('posters/', instance.slug, filename)


def get_manga_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('manga/', str(instance.volume.manga.slug), 'volume ' + str(instance.volume.volume),
                        filename)


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class MangaArtist(models.Model):
    name = models.CharField('Artist name', max_length=100, unique=True)
    slug = models.SlugField('url', unique=True, blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(MangaArtist, self).save(*args, **kwargs)


class Manga(models.Model):
    japan_name = models.CharField('Japan title', max_length=100, null=True, blank=True)
    english_name = models.CharField('English title', max_length=100)
    descriptions = models.TextField('Description', max_length=500)
    slug = models.SlugField('url', unique=True, blank=True)
    categories = ChoiceArrayField(
        models.CharField(choices=MANGA_CATEGORIES, max_length=15, blank=True), blank=True, null=True)
    artists = models.ManyToManyField(MangaArtist, verbose_name='Artists', blank=True)
    poster = models.ImageField('Poster', upload_to=get_poster_path, blank=True, null=True)
    rating = models.FloatField('Rating', default=0)
    is_promoted = models.BooleanField('Recommended', default=False)

    def __str__(self):
        return str(self.english_name) + ' | ' + str(self.slug)

    class Meta:
        verbose_name = 'Manga'
        verbose_name_plural = 'Mangas'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.english_name)
        super(Manga, self).save(*args, **kwargs)


class MangaVolume(models.Model):
    volume = models.IntegerField('Volume')
    create_time = models.DateTimeField('Upload date', auto_now_add=True)
    created_by = models.ForeignKey(User, verbose_name='Uploaded by user', on_delete=models.SET(get_sentinel_user),
                                   null=True)
    manga = models.ForeignKey(Manga, verbose_name='Manga', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Manga volume'
        verbose_name_plural = 'Manga volume'
        unique_together = ('volume', 'manga')

    def __str__(self):
        return str(self.manga) + ': ' + str(self.volume)


class MangaImage(models.Model):
    volume = models.ForeignKey(MangaVolume, verbose_name='Volume', on_delete=models.CASCADE)
    sort_index = models.IntegerField('position')
    image = models.ImageField('Image', upload_to=get_manga_image_path)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return str(self.volume.manga.english_name) + ': Volume - ' + str(self.volume.volume) + ' image ' + str(
            self.sort_index)


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


@receiver(post_delete, sender=MangaImage)
def delete_img_from_media(sender, instance, **kwargs):
    os.remove(os.path.join(settings.MEDIA_ROOT, instance.image.name))


@receiver(pre_save, sender=MangaImage)
def delete_file_on_change_extension(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_image = MangaImage.objects.get(pk=instance.pk).image
        except MangaImage.DoesNotExist:
            return
        else:
            new_image = instance.image
            if old_image and new_image.url != new_image.url:
                old_image.delete(save=False)
