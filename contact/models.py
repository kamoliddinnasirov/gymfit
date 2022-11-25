from django.core.validators import EmailValidator
from django.db import models
from home.models import BaseModel
from django.utils.translation import gettext_lazy as _


class ContactBannerModel(BaseModel):
    contact_title = models.CharField(max_length=20, null=True, blank=True, verbose_name=_("contact title"))
    contact_banner = models.ImageField(upload_to='media/contact_banner', null=True, blank=True, verbose_name=_('contact banner'))

    def __str__(self):
        return  self.contact_title

    class Meta:
        verbose_name = _('banner')
        verbose_name_plural = _('banners')


class ContactModel(BaseModel):
    phone = models.CharField(max_length=13)
    from_time = models.TimeField()
    to_time = models.TimeField()
    email = models.EmailField()
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.location

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')