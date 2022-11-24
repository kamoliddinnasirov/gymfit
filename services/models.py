from django.db import models
from blog.models import BaseModel
from django.utils.translation import gettext_lazy as _


class PeopleSay(BaseModel):
    title = models.CharField(max_length=50, verbose_name=_('title'))
    description = models.CharField(max_length=255, verbose_name=_('description'))
    author_name = models.CharField(max_length=50, verbose_name=_('author name'))
    job = models.CharField(max_length=50, verbose_name=_('job'))


    def __str__(self):
        return f"{self.title}, {self.author_name}, {self.job}"

    class Meta:
        verbose_name = _('What people say')
        verbose_name_plural = _('What people says')
