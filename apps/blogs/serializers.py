from rest_framework import serializers
from .models import Comment
from apps.blogs.models import BlogPost, BlogPostCategory, Category
from django.contrib.auth.models import User


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'body', 'created']

#
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "category_name"]

class BlogPostSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    categories = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)
    
    class Meta:
        model = BlogPost
        fields = ["id", "title", "description", "content", "user_id", "categories"]

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPostCategory
        fields = ["id", "blog_id", "category"]
