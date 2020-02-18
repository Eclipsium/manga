import os
import uuid

from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.core.files.base import ContentFile
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from pytils.translit import slugify

from sorl.thumbnail import get_thumbnail

from apps.manga_api.validators import validate_file_size_and_ext
from util import models

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


def get_archive_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('archive/', str(instance.manga.slug),
                        'volume ' + str(instance.volume),
                        filename)


def get_manga_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('manga/', str(instance.volume.manga.slug), 'volume ' + str(instance.volume.volume),
                        filename)


def get_sentinel_user():
    return get_user_model().objects.get_or_create(nickname='deleted')[0]


class Manga(models.Model):
    create_by_user = models.ForeignKey(User, verbose_name='Create by user', on_delete=models.SET(get_sentinel_user),
                                       null=True, blank=True)
    english_name = models.CharField('English title', max_length=100, unique=True)
    descriptions = models.TextField('Description', max_length=500, blank=True, null=True)
    slug = models.SlugField('url', unique=True, blank=True, null=True)
    artists = ArrayField(models.CharField(verbose_name='Artists', max_length=200), blank=True, null=True)
    poster = models.ImageField('Poster', upload_to=get_poster_path, blank=True)
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

    def save(self, *args, **kwargs):
        if not self.id:
            # Have to save the image (and imagefield) first
            super(MangaImage, self).save(*args, **kwargs)
            # obj is being created for the first time - resize

            resized = get_thumbnail(self.image, '720')
            # Manually reassign the resized image to the image field
            self.image.save(resized.name, ContentFile(resized.read()), True)

        super(MangaImage, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.volume.manga.english_name) + ': Volume - ' + str(self.volume.volume) + ' image ' + str(
            self.sort_index)


class MangaArchive(models.Model):
    manga = models.ForeignKey(Manga, null=True, verbose_name='Manga', on_delete=models.CASCADE)
    volume = models.IntegerField('volume', default=1)
    archive = models.FileField('Archive', upload_to=get_archive_path, validators=[validate_file_size_and_ext])

    class Meta:
        verbose_name = 'Archive'
        verbose_name_plural = 'Archives'

    def __str__(self):
        return str(self.manga.slug) + ' - ' + str(self.volume)


# Delete manga poster in media after delete manga object
@receiver(post_delete, sender=Manga)
def delete_img_from_media(sender, instance, **kwargs):
    os.remove(os.path.join(settings.MEDIA_ROOT, instance.poster.name))


# Delete manga archive in media after delete archive object
@receiver(post_delete, sender=MangaArchive)
def delete_arch_from_media(sender, instance, **kwargs):
    os.remove(os.path.join(settings.MEDIA_ROOT, instance.archive.name))


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
