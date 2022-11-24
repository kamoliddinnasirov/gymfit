from django.urls import path
from pages.views import TrainerView

app_name = 'pages'

urlpatterns = [
    path('trainers/', TrainerView.as_view(), name="trainer"),
]