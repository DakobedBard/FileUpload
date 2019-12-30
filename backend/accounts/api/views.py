from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.filters import (SearchFilter, OrderingFilter)
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin


