from rest_framework import generics
from apps.blogs.models import BlogPost
from apps.blogs.serializers import BlogPostSerializer


class BlogPostCreatGetView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    # TODO: Must be added after Implementing the Authentication
    permission_classes = []


class BlogPostOneView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "id"
    # TODO: Must be added after Implementing the Authentication
    permission_classes = []
