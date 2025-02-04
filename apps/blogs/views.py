from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Blog, Comment
from .serializers import CommentSerializer

class CommentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, blog_id, comment_id):
        try:
            blog = Blog.objects.get(pk=blog_id)
        except Blog.DoesNotExist:
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
