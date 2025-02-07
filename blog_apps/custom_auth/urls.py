from django.urls import path

from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from .views import logout

urlpatterns = [
    path('token', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/',logout, name ='logout'),
    path('register', views.RegisterView.as_view(), name='register'),
]
