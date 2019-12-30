from django.urls import path
from backend.uploadapp.api.views import *

urlpatterns = [
    path('', FileUploadView.as_view())
]