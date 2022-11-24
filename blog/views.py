from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, CreateView, DetailView
from blog.models import PostModel, BlogGridModel, AuthorModel, PostTagModel, BlogGridModel, CommentModel
from blog.forms import CommentModelForm

class PostListView(ListView):
    template_name = 'blog/blog-sidebar.html'

    def get_queryset(self):
        qs = PostModel.objects.order_by('-id')
        tag = self.request.GET.get('tag', None)
        if tag:
            qs = qs.filter(tag__name=tag)
        return qs

    # def get_context_data(self,  **kwargs):

class PostDetailView(DetailView):
    model = PostModel
    template_name = 'blog/blog-single.html'


class CommentCreateView(CreateView):
    form_class = CommentModelForm

    def form_valid(self, form):
        print(form.instance)
        form.instance.post = get_object_or_404(PostModel, pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail', kwargs={'pk': self.kwargs.get('pk')})
