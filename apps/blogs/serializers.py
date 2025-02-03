from rest_framework import serializers
from apps.blogs.models import BlogPost
from apps.custom_auth.models import User


class BlogPostSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = BlogPost
        fields = ["id", "title", "description", "content", "user_id"]
