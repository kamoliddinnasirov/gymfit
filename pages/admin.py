from django.contrib import admin
from django.contrib.admin import TabularInline


from pages.models import PopularTrainer, AboutBanner, GalleryMain, Gallery, TrainerBanner, Weeks, Category, OurTrainer, \
    CourseBanner, PopularCourseGallery, PopularCourse, Mentor, TrainerGallery


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


class ImageInline(admin.TabularInline):  # TabularInline ForeignKey bilan birgalikda ishlidi
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


@admin.register(TrainerBanner)
class TrainerBannerAdmin(admin.ModelAdmin):
    list_display = ('trainer_title',)
    list_display_links = ('trainer_title',)
    list_filter = ('created_at',)


@admin.register(Weeks)
class WeekAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    list_filter = ('created_at',)


class TrainerGalleryAdmin(TabularInline):
    model = TrainerGallery

@admin.register(OurTrainer)
class OurTrainerAdmin(admin.ModelAdmin):
    inlines = [
        TrainerGalleryAdmin,
    ]
    list_display = ('full_name', 'category')
    list_display_links = ('full_name', 'category')
    search_fields = ('full_name', 'category')


@admin.register(CourseBanner)
class CourseBannerAdmin(admin.ModelAdmin):
    list_display = ('courses_title',)
    list_display_links = ('courses_title',)
    list_filter = ('created_at',)


class CourseGallery(TabularInline):
    model = PopularCourseGallery


class MentorAdmin(TabularInline):
    model = Mentor


@admin.register(PopularCourse)
class PopCourse(admin.ModelAdmin):
    list_display = ('course',)
    list_display_links = ('course',)
    inlines = [
        MentorAdmin,
        CourseGallery,

    ]