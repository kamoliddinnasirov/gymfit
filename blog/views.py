from django.shortcuts import render
from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'pages/about.html'

class HomeView(TemplateView):
    template_name = 'home/index.html'

class BlogView(TemplateView):
    template_name = 'blog/blog.html'

class BlogSView(TemplateView):
    template_name = 'blog/blog-sidebar.html'

class BlogSiView(TemplateView):
    template_name = 'blog/blog-single.html'

class PriceView(TemplateView):
    template_name = 'membership/pricing.html'

class ContactView(TemplateView):
    template_name = 'contact.html'