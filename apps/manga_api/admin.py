from django.contrib import admin

# Register your models here.
from apps.manga_api.models import *


@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    pass


@admin.register(MangaVolume)
class MangaAdmin(admin.ModelAdmin):
    pass


@admin.register(MangaImage)
class MangaAdmin(admin.ModelAdmin):
    pass


@admin.register(MangaArchive)
class MangaAdmin(admin.ModelAdmin):
    pass


