from django.urls import path
from pages.views import TrainerView, AboutView, CourseView

app_name = 'pages'

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('trainers/', TrainerView.as_view(), name="trainer"),
    path('course/', CourseView.as_view(), name='course')
]