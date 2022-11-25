from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from pages.models import AboutBanner, PopularTrainer, GalleryMain, TrainerBanner, \
    Weeks, Category, OurTrainer, CourseBanner, PopularCourse, CourseSingleBanner, CSingle, Feature, Gallery, \
    TrainerGallery, Mentor, PopularCourseGallery


class AboutView(TemplateView):
    template_name = "pages/about.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['about_banner'] = AboutBanner.objects.order_by('-pk')[:2]
        data['popular_trainers'] = PopularTrainer.objects.order_by('-pk')[:1]
        data['gallery_main'] = GalleryMain.objects.all()
        data['gallery'] = Gallery.objects.order_by('-pk')[:8]
        return data


class TrainerView(TemplateView):
    template_name = "pages/trainer.html"
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['trainer_banners'] = TrainerBanner.objects.order_by('-pk')[:1]
        data['our_trainer'] = OurTrainer.objects.all()
        data['gallery'] = TrainerGallery.objects.all()
        data['categories'] = Category.objects.all()
        return data

class CourseView(TemplateView):
    template_name = "pages/course.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['course_banner'] = CourseBanner.objects.order_by('-pk')[:1]
        data['popular_courses'] = PopularCourse.objects.all()
        data['weeks'] = Weeks.objects.all()
        data['ments'] = Mentor.objects.all()
        data['images'] = PopularCourseGallery.objects.all()
        return data

class CourseSingleView(TemplateView):
    template_name = "pages/course-single.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['course_s_banner'] = CourseSingleBanner.objects.order_by('-pk')[:1]
        data['course_single'] = CSingle.objects.all()
        data['price'] = Feature.objects.all()
        return data


