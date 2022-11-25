from django.db import models
from home.models import BaseModel
from django.utils.translation import gettext_lazy as _


class  Package(BaseModel):
    title = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('title'))
    services = models.CharField(max_length=50, verbose_name=_('services'))
    continue_package = models.CharField(max_length=50, verbose_name=_("continue package"))
    price = models.PositiveIntegerField()
    check_close = models.BooleanField(help_text="(0)-close, (1)-check", verbose_name=_('check close'))
    popular = models.BooleanField(help_text=_("(check)-popular"))


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('package')
        verbose_name_plural = _ ('packages')


# class Service(BaseModel): # admin.py TabularInline
#     service = models.ForeignKey(Package, on_delete=models.CASCADE, verbose_name=_("service"))
#
#
#     def __str__(self):
#         return self.services
#
#     class Meta:
#         verbose_name = _("service")
#         verbose_name_plural = _("services")