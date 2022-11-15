from django.urls import path
from blog.views import PostListView, CommentCreateView, PostDetailView

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='detail'),
    # path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment'),
    # path('blog/', BlogView.as_view()),
]
