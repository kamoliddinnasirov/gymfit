from django.shortcuts import render
from django.views.generic import ListView

from pages.models import PopularTrainer



class PopListView(ListView):
    model = PopularTrainer
    template_name = 'pages/about.html'
