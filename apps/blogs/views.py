from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import BlogPost, Likes
from .serializers import Likesserializer

class LikeUnlikeBlogPostView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, blog_id):
        blog = get_object_or_404(BlogPost, id=blog_id)
        like, created = Likes.objects.get_or_create(user_id=request.user, blog_id=blog)
        
        if not created:
            return Response({'detail': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = Likesserializer(like)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def delete(self, request, blog_id):
        blog = get_object_or_404(BlogPost, id=blog_id)
        like = Likes.objects.filter(user_id=request.user, blog_id=blog)
        
        if not like.exists():
            return Response({'detail': 'You have not liked this post yet.'}, status=status.HTTP_400_BAD_REQUEST)
        
        like.delete()
        return Response({'detail': 'Blog post unliked successfully!'}, status=status.HTTP_204_NO_CONTENT)
