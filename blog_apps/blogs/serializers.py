from rest_framework import serializers
from blog_apps.custom_auth.models import User
from .models import BlogPost,Likes, BlogPostCategory, Category, Comment

class Likesserializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    blog_id = serializers.PrimaryKeyRelatedField(queryset=BlogPost.objects.all())
    class Meta:
        model = Likes
        fields = '__all__'


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
