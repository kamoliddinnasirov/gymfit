

from django.contrib import admin
from django.template.defaultfilters import title

from home.models import Navbar, Footer, Home,  HomeCategory

@admin.register(Navbar)
class NavbarAdmin(admin.ModelAdmin):
    list_display = ('brand_name', 'phone_number')
    list_display_links = ('brand_name',)
    list_filter = ('created_at',)

@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ('address', 'support_phone', 'support_mail',)
    list_display_links = ('address', 'support_phone', 'support_mail',)
    list_filter = ('address', 'created_at')

class HomeCategoryAdmin(admin.TabularInline):
    model = HomeCategory

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('club_name',)
    list_display_links = ('club_name',)
    list_filter = ('created_at',)
    inlines = [
        HomeCategoryAdmin,
    ]



