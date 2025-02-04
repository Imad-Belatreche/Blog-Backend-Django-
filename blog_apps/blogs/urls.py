from django.urls import path
from .views import LikeUnlikeBlogPostView
from . import views


urlpatterns = [
    path("", views.BlogPostCreateListView.as_view()),
    path("<int:id>/", views.BlogPostOneView.as_view()),
    path('blogs/<int:blog_id>/comments/<int:comment_id>/', views.CommentView.as_view(), name='comment-detail'),
    path('blogs/<int:blog_id>/like/<int:user_id>', LikeUnlikeBlogPostView.as_view(), name='like-unlike-blog'),
]
