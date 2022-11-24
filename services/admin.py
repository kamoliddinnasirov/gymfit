from django.contrib import admin
from services.models import PeopleSay

@admin.register(PeopleSay)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name', 'job')
    list_display_links = ('title', 'author_name', 'job')
    search_fields = ('author_name', 'job')

