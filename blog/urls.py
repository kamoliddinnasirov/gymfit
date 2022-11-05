from django.urls import path
from .views import PostListView, CommentCreateView

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment'),
    # path('blog/', BlogView.as_view()),

]
