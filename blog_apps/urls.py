from django.urls import include, path


urlpatterns = [
    path("blogs/", include("blog_apps.blogs.urls")),
    path("auth/", include("blog_apps.custom_auth.urls"))
]
