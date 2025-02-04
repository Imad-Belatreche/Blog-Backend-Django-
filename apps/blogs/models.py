from django.conf import settings
from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True, null=False)

    def __str__(self):
        return self.category_name


class BlogPost(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=True)
    content = models.TextField()
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, through="BlogPostCategory")

    def __str__(self):
        return f"{self.__class__.__name__}: Title \"{self.title}\""


class BlogPostCategory(models.Model):
    blog_id = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"Categories:{self.category_id} \nBlog: {self.blog_id}"
