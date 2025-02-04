from django.urls import path
from . import views


urlpatterns = [
    path("", views.BlogPostCreateListView.as_view()),
    path("<int:id>/", views.BlogPostOneView.as_view())
]
