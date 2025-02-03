from django.conf import settings
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=120, blank=False)
    description = models.CharField(blank=True, max_length=200)
    content = models.TextField()
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.__class__.__name__}: Title \"{self.title}\""
