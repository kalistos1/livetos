from itertools import combinations_with_replacement
from django.contrib import admin
from .models import Post,Comment


# Register your models here.
class AdminPost(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'author', 'date_created')

class AdminComment(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'text', 'date_created')


admin.site.register(Post, AdminPost)
admin.site.register(Comment, AdminComment)