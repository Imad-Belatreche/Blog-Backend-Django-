from django.urls import path
from . import views


urlpatterns = [
    path("", views.BlogPostCreatGetView.as_view()),
    path("<int:id>/", views.BlogPostOneView.as_view())
]
