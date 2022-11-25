from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from membership.models import Package


class MembershipView(ListView):
    model = Package
    template_name = 'membership/pricing.html'

    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data(**kwargs)
    #     data['packages'] = Package.objects.all()
    #     data['service'] = Service.objects.all()
    #     return data
