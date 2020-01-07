from django.contrib import admin

# Register your models here.
from apps.rating_api.models import Vote


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    pass
