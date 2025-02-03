from rest_framework import serializers
from apps.blogs.models import BlogPost

#TODO: WARNING! For testing only
from django.contrib.auth.models import User
#

class BlogPostSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = BlogPost
        fields = ["id", "title", "description", "content", "user_id"]
