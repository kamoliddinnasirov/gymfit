from django.contrib import admin
from membership.models import Package


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    list_display_links = ('title', 'price')
    search_fields = ('title', 'price')
