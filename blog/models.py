from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class AuthorModel(models.Model):
    full_name = models.CharField(max_length=100, verbose_name=_('full name'))

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')


class ArticleModel(BaseModel):
    article = models.TextField(verbose_name=_('article'))

    def __str__(self):
        return self.article

    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')

class PostTagModel(BaseModel):
    name = models.CharField(max_length=30, verbose_name=_('name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class BlogGridModel(models.Model):
    blog_title = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('banner title'))

    def __str__(self):
        return self.blog_title

    class Meta:
        verbose_name = _('BlogGridTitle')
        verbose_name_plural = _('BlogGridTitles')


class PostModel(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    trainer_image = models.ImageField(upload_to='trainer/', verbose_name=_('trainer image'))
    article = models.ForeignKey(ArticleModel, on_delete=models.RESTRICT, verbose_name=_("article"))
    main_image = models.ImageField(upload_to='main_images/', verbose_name=_('main image'))
    body = models.TextField(verbose_name=_('body'))
    advice = models.TextField(verbose_name=_('advice'))
    auther = models.ForeignKey(AuthorModel, related_name='posts', on_delete=models.RESTRICT, verbose_name=_("auther"))
    tag = models.ManyToManyField(PostTagModel, related_name='posts', verbose_name=_('tag'))

    def __str__(self):
        return f"{self.title[:50]} ..."

    class Meta:
        ordering = ('-id',)
        verbose_name = _('blog post')
        verbose_name_plural = _('blog posts')


class CommentModel(BaseModel):
    # name = models.CharField(max_length=255, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    comment = models.TextField(verbose_name=_('comment'))
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments', verbose_name=_('post'))
    reply = models.ForeignKey('CommentModel', on_delete=models.CASCADE,  blank=True, null=True, verbose_name=_('reply'))
    auth = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('auth'))

    def __str__(self):
        return f"{self.auth}\n{self.email}\n{self.comment}"

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
