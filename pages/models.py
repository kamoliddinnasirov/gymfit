from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from home.models import BaseModel
import datetime
from django.core.validators import MaxValueValidator


# ================================About==================
class AboutBanner(BaseModel):
    about_title = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('about title'))
    about_banner = models.ImageField(upload_to='about_banner/%Y/%m/%d/', null=True, blank=True,
                                     verbose_name=_('about banner'))

    def __str__(self):
        return f"{self.about_title}"

    class Meta:
        verbose_name = _('About Banner')
        verbose_name_plural = _('About Banner')


class PopularTrainer(BaseModel):
    image1 = models.ImageField(upload_to='popular_people/%Y/%m/%d/', verbose_name=_('1 image'))
    image2 = models.ImageField(upload_to='popular_people2/%Y/%m/%d/', verbose_name=_('2 image'))
    started = models.PositiveIntegerField(validators=[MaxValueValidator(4)], verbose_name=_('started'))
    people_about = RichTextUploadingField(max_length=50, verbose_name=_('people about'))

    def get_experience_date(self):
        experience = datetime.date.today()
        year = experience.year
        experience = year - self.started
        return experience

    def __str__(self):
        return f"{self.people_about[:15]}"

    class Meta:
        verbose_name = _('Popular Trainer')
        verbose_name_plural = _('Popular Trainers')


class GalleryMain(BaseModel):
    title = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('title'))
    sub_title = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('sub title'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('gallery main')
        verbose_name_plural = _('gallery main')


class Gallery(BaseModel):
    gallery = models.ForeignKey(GalleryMain, on_delete=models.RESTRICT)
    image = models.ImageField(upload_to='about_gallery/%Y/%m/%d/', default='some_value', verbose_name=_('image'))
    is_active = models.BooleanField(default=False, verbose_name=_('is_active'))

    def __str__(self):
        return self.gallery

    class Meta:
        verbose_name = _("gallery")
        verbose_name_plural = _('gallery')


# ===================================About end==========================

# ===============================Trainer ====================
class TrainerBanner(BaseModel):
    trainer_title = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('trainer title'))
    trainer_banner = models.ImageField(upload_to='trainer_banner/%Y/%m/%d/', null=True, blank=True,
                                       verbose_name=_('trainer banner'))

    def __str__(self):
        return self.trainer_title

    class Meta:
        verbose_name = _('trainer banner')
        verbose_name_plural = _('trainer banners')

class Weeks(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_('name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('week')
        verbose_name_plural = _('weeks')


class Category(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_("name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class OurTrainer(BaseModel):
    full_name = models.CharField(max_length=255, verbose_name=_('full name'))
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, verbose_name=_('category'))
    achievement = models.CharField(max_length=100, verbose_name=_('achievement'))
    facebook = models.URLField()
    twitter = models.URLField()
    linkedin = models.URLField()
    # image = TubalarInline

    def __str__(self):
        return f"{self.full_name}, {self.category}"

    class Meta:
        verbose_name = _('Our trainer')
        verbose_name_plural = _('Our trainer')

class TrainerGallery(BaseModel):
    gallery = models.ForeignKey(OurTrainer, on_delete=models.RESTRICT, verbose_name=_('gallery'))
    image = models.ImageField(upload_to='TrainerGallery/', default='some_value')
    is_active = models.BooleanField(default=False, verbose_name=_('is_active'))

    def __str__(self):
        return self.gallery

    class Meta:
        verbose_name = _("gallery")
        verbose_name_plural = _('gallery')


class CourseBanner(BaseModel):
    courses_title = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('courses title'))
    courses_banner = models.ImageField(upload_to='courses_banner/%Y/%m/%d/', null=True, blank=True,
                                       verbose_name=_('courses banner'))

    def __str__(self):
        return self.courses_title

    class Meta:
        verbose_name = _('course banner')
        verbose_name_plural = _('courses banner')


class PopularCourse(BaseModel):
    # title = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('title'))
    course = models.ForeignKey(Category, on_delete=models.RESTRICT, verbose_name=_('course'))
    # mentor = TabularInline
    weeks = models.ManyToManyField(Weeks, verbose_name=_('weeks'))
    from_time = models.TimeField(auto_now=False, verbose_name=_('from time'))
    to_time = models.TimeField(auto_now=False, verbose_name=_('to time'))
    # main_banner = TabularInline

    def __str__(self):
        return f"{self.weeks}"

    class Meta:
        verbose_name = _('popular course')
        verbose_name_plural = _('popular courses')


class Mentor(BaseModel): # admin.py TabularInline uchun
    name = models.ForeignKey(PopularCourse, on_delete=models.RESTRICT, verbose_name=_('name'))
    full_name = models.CharField(max_length=50, verbose_name=_('full_name'))
    is_active = models.BooleanField(default=False, verbose_name=_('is_active'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("mentor")
        verbose_name_plural = _('mentors')


class PopularCourseGallery(BaseModel):  # admin.py TabularInline uchun
    gallery = models.ForeignKey(PopularCourse, on_delete=models.RESTRICT,  verbose_name=_('gallery'))
    image = models.ImageField(upload_to='PopularCourseGallery/', default='some_value')
    is_active = models.BooleanField(default=False, verbose_name=_('is_active'))

    def __str__(self):
        return self.gallery

    class Meta:
        verbose_name = _("gallery")
        verbose_name_plural = _('gallery')


# =========================Course Single==================

class CourseSingleBanner(BaseModel):
    course_single_title = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('course_single_title'))
    course_single_banner = models.ImageField(upload_to='courses_single_banner/%Y/%m/%d/', null=True, blank=True,
                                       verbose_name=_('course_single_banner'))

    def __str__(self):
        return self.course_single_title

    class Meta:
        verbose_name = _('Course Single Banner')
        verbose_name_plural = _('Course Single Banners')

class CSingle(BaseModel):
    hours = models.CharField(max_length=50, verbose_name=_('hours'))
    calories_count = models.PositiveIntegerField(verbose_name=_('calories count'))
    type_calories = models.CharField(max_length=50, verbose_name=_('type calories'))
    workout_count = models.PositiveIntegerField(verbose_name=_('workout count (%)'))
    type_workout = models.CharField(max_length=50, verbose_name=_('type workout'))
    body = models.TextField(verbose_name=_('body'))

    def __str__(self):
        return f"{self.type_workout}"

    class Meta:
        verbose_name = _('Course Single')
        verbose_name_plural = _('Course Single')

class Feature(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, verbose_name=_('category'))
    duration = models.PositiveIntegerField(verbose_name=_('duration'))
    students = models.PositiveIntegerField(verbose_name=_('students'))
    shift = models.CharField(max_length=50, verbose_name=_('shift'))
    price = models.PositiveIntegerField(verbose_name=_('price'))

    def __str__(self):
        return  f"{self.category}, {self.students}, {self.price}"

    class Meta:
        verbose_name = _('Feature')
        verbose_name_plural = _('Features')

