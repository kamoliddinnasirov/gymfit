from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view()),
    path('about/', AboutView.as_view()),
    path('blog/', BlogView.as_view()),
    path('blog-sidebar/', BlogSView.as_view()),
    path('blog-single/', BlogSiView.as_view()),
    path('membership/', PriceView.as_view()),
    path('contact/', ContactView.as_view()),
]
