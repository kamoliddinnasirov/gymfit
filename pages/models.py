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
    image = models.ImageField(upload_to='about_gallery/%Y/%m/%d/', verbose_name=_('image'))
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

class OurTrainer(BaseModel):
    full_name = models.CharField(max_length=255, verbose_name=_('full name'))
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, verbose_name=_('category'))
    achievement = models.CharField(max_length=100, verbose_name=_('achievement'))
    facebook = models.URLField()
    twitter = models.URLField()
    linkedin = models.URLField()
    image = models.ImageField(upload_to='trainer_photo/%Y/%m/%d/', verbose_name=_('image'))

    def __str__(self):
        return f"{self.full_name}, {self.category}"

    class Meta:
        verbose_name = _('Our trainer')
        verbose_name_plural = _('Our trainer')

