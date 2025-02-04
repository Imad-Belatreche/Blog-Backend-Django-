from django.db import models
from apps.blogs.models import Blog 
from django.contrib.auth.models import User 


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=120, blank=False)
    description = models.CharField(blank=True, max_length=200)
    content = models.TextField()
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.__class__.__name__}: Title \"{self.title}\""


class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
         return f"Comment from {self.user} - {self.content}"
    
