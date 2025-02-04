from django.contrib import admin
from .models import Comment, Likes, BlogPost, Category, BlogPostCategory

# Register your models here.
admin.site.register(Comment)
admin.site.register(Likes)
admin.site.register(Category)
admin.site.register(BlogPost)
admin.site.register(BlogPostCategory)