from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from services.models import PeopleSay

class ServiceView(ListView):
    template_name = 'services/service.html'
    model = PeopleSay




