from django.contrib import admin

# Register your models here.
from apps.comment_api.models import Comments


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    pass
