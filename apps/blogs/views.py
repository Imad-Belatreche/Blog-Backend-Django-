from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status, filters
from .models import BlogPost, Comment, Likes
from .serializers import CommentSerializer, Likesserializer, BlogPostSerializer
from django.http import Http404
from django.shortcuts import get_object_or_404
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


class CommentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, blog_id, comment_id):
        try:
            blog = BlogPost.objects.get(pk=blog_id)
        except BlogPost.DoesNotExist:
            return Response({'error': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(blog=blog, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, blog_id, comment_id):
        try:
            comment = Comment.objects.get(pk=comment_id, blog_id=blog_id, user=request.user)
        except Comment.DoesNotExist:
            return Response({'error': 'Comment not found or unauthorized'}, status=status.HTTP_404_NOT_FOUND)

        comment.delete()
        return Response({'message': 'Comment deleted successfully'}, status=status.HTTP_200_OK)


class BlogPostCreateListView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    # Adds search functionality using the title field
    # and the api call is /api/blogs/?search=something
    
    search_fields = ['title']
    filter_backends = [filters.SearchFilter]

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        else:
            return []

    def handle_exception(self, exc):
        if isinstance(exc, Http404):
            return Response({"error": "Blog posts not found"},
                            status=status.HTTP_404_NOT_FOUND)
        return super().handle_exception(exc)


class BlogPostOneView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "id"

    def get_permissions(self):
        if self.request.method in ["PUT", "DELETE", "PATCH"]:
            return []
        else:
            return [IsAuthenticated()]

    def get_object(self):
        try:
            return get_object_or_404(BlogPost, id=self.kwargs["id"])
        except Http404:
            raise Http404("Blog post with this ID does not exist.")

    def handle_exception(self, exc):
        if isinstance(exc, Http404):
            return Response(
                {"error": "Blog post not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        return super().handle_exception(exc)
