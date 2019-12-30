from django.conf.urls import url, include
from django.urls import path, include, re_path
from accounts.api.views import UserLoginView, UserCreateAPIView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    re_path(r'register/$', UserCreateAPIView.as_view(), name='register'),
    re_path(r'login/', UserLoginView.as_view(),name='login'),
    re_path(r'token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
]