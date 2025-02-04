from rest_framework import serializers
from django.contrib.auth.models import User
from .models import BlogPost,Likes

class Likesserializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    blog_id = serializers.PrimaryKeyRelatedField(queryset=BlogPost.objects.all())
    class Meta:
        model = Likes
        fields = '__all__'