from django.contrib import admin
from home.models import Navbar, Footer, Home, PeopleSay

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

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('club_name', 'home_title', 'home_cat_name', )
    list_display_links = ('club_name', 'home_title', 'home_cat_name', )
    search_fields = ('home_cat_name',)
    list_filter = ('created_at',)

@admin.register(PeopleSay)
class PeopleSayAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'title', 'sub_title', 'job')
    list_display_links = ('author_name', 'title', 'sub_title', 'job')
    search_fields = ('author_name',)
    list_filter = ('created_at',)
