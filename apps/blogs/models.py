from django.db import models
from django.conf import settings

# Create your models here.
class Likes(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog_id = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('user_id','blog_id')