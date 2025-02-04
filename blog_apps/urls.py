from django.urls import include, path


urlpatterns = [
    path("blogs/", include("apps.blogs.urls")),
    path("auth/", include("apps.custom_auth.urls"))
]
