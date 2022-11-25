from django.contrib import admin
from membership.models import Package, Service


class ServiceAdmin(admin.TabularInline):
    model = Service
@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    list_display_links = ('title', 'price')
    search_fields = ('title', 'price')
    inlines = [
        ServiceAdmin,
    ]
