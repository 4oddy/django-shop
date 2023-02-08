from django.contrib import admin
from .models import Blog, Comments


@admin.register(Blog)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'blog')

