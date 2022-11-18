from django.contrib import admin
from pages.models import PopularTrainer, AboutBanner, GalleryMain, Gallery

@admin.register(PopularTrainer)
class PopularTrainerAdmin(admin.ModelAdmin):
    list_display = ('started', 'created_at', 'updated_at')
    list_display_links = ('started',)
    search_fields = ('people_about',)
    list_filter = ('created_at',)

@admin.register(AboutBanner)
class AboutBannerAdmin(admin.ModelAdmin):
    list_display = ('about_title', 'created_at')
    list_display_links = ('about_title',)
    list_filter = ('created_at',)


class ImageInline(admin.TabularInline): #TabularInline ForeignKey bilan birgalikda ishlidi
    model = Gallery

@admin.register(GalleryMain)
class GalleryMainAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    list_display = ('title', 'sub_title')
    list_display_links = ('title', 'sub_title')
    search_fields = ('title', 'sub_title')
    list_filter = ('created_at',)











