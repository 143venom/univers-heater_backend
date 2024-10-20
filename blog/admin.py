from django.contrib import admin
from .models import Blog, Comment


@admin.register(Blog)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'slug', 'created_at', 'updated_at')
    search_fields = ('title', 'author')
    list_filter = ('created_at',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'blog', 'created_at')
    search_fields = ('author', 'content')
    list_filter = ('created_at',)