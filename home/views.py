from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from services.models import PeopleSay
from home.models import Navbar, Footer, Home, HomeCategory


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['homes'] = Home.objects.all()
        data['categories'] = HomeCategory.objects.order_by('pk')[:3]
        data['people_say'] = PeopleSay.objects.all()
        return data


class BaseView(TemplateView):
    template_name = "layouts/base.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['navbar'] = Navbar.objects.order_by('-pk')
        data['footer'] = Footer.objects.all()
        return data

