from django.urls import path
from .views import CommentView

urlpatterns = [
    path('blogs/<int:blog_id>/comments/<int:comment_id>/', CommentView.as_view(), name='comment-detail'),
]
