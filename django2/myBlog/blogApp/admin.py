from django.contrib import admin
from .models import Post, Category, Comment, Follow


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Follow)
