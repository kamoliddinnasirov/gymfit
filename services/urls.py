from django.urls import path

from services.views import ServiceView

app_name = 'services'

urlpatterns = [
    path('', ServiceView.as_view(), name='service'),
]