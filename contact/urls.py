from django.urls import path

from contact.views import ContactSendView

app_name = 'contact'

urlpatterns = [
    path('', ContactSendView.as_view(), name='contact'),
]