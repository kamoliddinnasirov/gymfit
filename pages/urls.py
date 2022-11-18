from django.urls import path
from pages.views import PopListView

app_name = 'pages'

urlpatterns = [
    path('ab/', PopListView.as_view())
]