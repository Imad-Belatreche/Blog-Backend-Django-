from django.urls import path
from .views import LikeUnlikeBlogPostView

urlpatterns = [
    path('blogs/<int:blog_id>/like/<int:user_id>', LikeUnlikeBlogPostView.as_view(), name='like-unlike-blog'),
]
