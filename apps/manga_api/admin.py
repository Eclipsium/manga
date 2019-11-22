from django.contrib import admin

# Register your models here.
from apps.manga_api.models import *


@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    pass


# @admin.register(MangaPerson)
# class MangaPersonAdmin(admin.ModelAdmin):
#     pass

