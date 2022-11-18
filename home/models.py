from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Navbar(BaseModel):
    brand_name = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('brand name'))
    nav_item = models.CharField(max_length=10, null=True, blank=True, verbose_name=_('navbar item'))
    phone_number = models.CharField(max_length=9, null=True, blank=True, verbose_name=_('phone number'))


    def __str__(self):
        return f"{self.brand_name}, {self.nav_item}, {self.phone_number}"

    class Meta:
        verbose_name = _('navbar')
        verbose_name_plural = _('navbar')


class Footer(BaseModel):
    title_location = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('title location'))
    address = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('address'))
    support_phone = models.CharField(max_length=13, null=True, blank=True, verbose_name=_('support_phone'))
    support_mail = models.EmailField(null=True, blank=True, verbose_name=_('support_phone'))

    def __str__(self):
        return f"{self.address}, {self.support_phone}, {self.support_mail}"

    class Meta:
        verbose_name = _('footer')
        verbose_name_plural = _('footer')


class Home(BaseModel):
    club_name = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('club name'))
    home_title = RichTextUploadingField(max_length=40, null=True, blank=True, verbose_name=_('home title'))
    home_banner = models.ImageField(upload_to='home_banner/%Y/%m/%d/', null=True, blank=True, verbose_name=_('home banner'))
    home_cat_name = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('home category name'))
    cat_description = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('category description'))

    def __str__(self):
        return f"{self.home_title}"

    class Meta:
        verbose_name = _('Home')
        verbose_name_plural = _('Home')


class PeopleSay(BaseModel):
    title = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('title'))
    sub_title = models.CharField(max_length=50, verbose_name=_('sub_title'))
    description = models.CharField(max_length=255, verbose_name=_('description'))
    author_name = models.CharField(max_length=50, verbose_name=_('author_name'))
    job = models.CharField(max_length=50, verbose_name=_('job'))


    def __str__(self):
        return f"{self.sub_title}, {self.author_name}, {self.job}"

    class Meta:
        verbose_name = _('What people say')
        verbose_name_plural=_('What people says')

