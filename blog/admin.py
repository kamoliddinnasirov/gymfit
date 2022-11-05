from django.contrib import admin
from .models import *


@admin.register(PostTagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    list_filter = ('created_at',)
    search_fields = ('name',)




@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'auther', 'blog_title', 'created_at')
    list_display_links = ('title', 'blog_title', 'auther')
    list_filter = ('created_at',)
    search_fields = ('title', 'body')
    autocomplete_fields = ('auther', 'tag')


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_display_links = ('name', 'email')
    list_filter = ('created_at',)


@admin.register(AuthorModel)
class AutherModelAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
    list_display_links = ('full_name',)
    search_fields = ('full_name',)
