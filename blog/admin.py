from django.contrib import admin
from blog.models import PostTagModel, BlogGridModel, PostModel, CommentModel, AuthorModel, ArticleModel


@admin.register(PostTagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article',)
    list_display_links = ('article',)


@admin.register(BlogGridModel)
class BlogGridAdmin(admin.ModelAdmin):
    list_display = ('blog_title',)
    list_display_links = ('blog_title',)


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'auther', )
    list_display_links = ('title', 'auther')
    search_fields = ('title', 'body')
    autocomplete_fields = ('auther', 'tag')


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('email',)
    list_display_links = ('email',)
    search_fields = ('comment',)

@admin.register(AuthorModel)
class AutherModelAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
    list_display_links = ('full_name',)
    search_fields = ('full_name',)
