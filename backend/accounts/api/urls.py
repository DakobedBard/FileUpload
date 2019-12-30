from django.conf.urls import url, include
from django.urls import path, include, re_path
from rest_framework_simplejwt import views as jwt_views
from .views import UserLoginView
urlpatterns = [
    re_path(r'token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path('login',UserLoginView.as_view(), name='login'),
]