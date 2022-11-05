from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, CreateView
from .models import PostModel
from .forms import CommentModelForm




class PostListView(ListView):
    model = PostModel
    template_name = 'blog/blog.html'

    def get_queryset(self):
        qs = PostModel.objects.order_by('-id')
        tag = self.request.GET.get('tag')
        if tag:
            qs = qs.filter(tag__name=tag)
        return qs


class CommentCreateView(CreateView):
    form_class = CommentModelForm

    def form_valid(self, form):
        print(form.instance)
        form.instance.post = get_object_or_404(PostModel, pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail', kwargs={'pk': self.kwargs.get('pk')})


