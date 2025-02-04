from django.http import Http404
from rest_framework import generics, status, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.blogs.models import BlogPost
from apps.blogs.serializers import BlogPostSerializer


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
