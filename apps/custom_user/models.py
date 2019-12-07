import os
import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


def get_avatar_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('profiles/', str(instance.nickname), filename)


def get_default_avatar():
    filename = 'default.jpg'
    return  os.path.join('profiles/', filename)


class UserAccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email address must be provided')

        if not password:
            raise ValueError('Password must be provided')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = UserAccountManager()

    email = models.EmailField('email', unique=True, blank=False, null=False)
    full_name = models.CharField('Полное имя', blank=True, null=True, max_length=400)
    nickname = models.CharField('Ник', blank=True, null=True, max_length=100, unique=True)
    is_staff = models.BooleanField('Админинстратор', default=False)
    is_verified = models.BooleanField('Верифицированый', default=False)  # Add the `is_verified` flag
    verification_uuid = models.UUIDField('Уникальный ключ', default=uuid.uuid4)
    is_active = models.BooleanField('Активный', default=True)
    avatar = models.ImageField('Аватарка', upload_to=get_avatar_path, default=get_default_avatar)

    def get_short_name(self):
        return self.nickname

    def get_full_name(self):
        return self.nickname

    def __unicode__(self):
        return self.nickname

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


@receiver(pre_save, sender=User)
def delete_file_on_change_extension(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_avatar = User.objects.get(pk=instance.pk).avatar
        except User.DoesNotExist:
            return
        else:
            new_avatar = instance.avatar
            if old_avatar and old_avatar.url != new_avatar.url:
                old_avatar.delete(save=False)
