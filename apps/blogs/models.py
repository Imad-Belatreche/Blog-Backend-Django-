from django.db import models
from django.contrib.auth.models import User
from .models import BlogPost 


# Create your models here.

class Comment(models.Model):
    blog = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
         return f"Comment from {self.user} - {self.content}"
    
