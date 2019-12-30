from .serializers import UserLoginSerializer
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.response import Response

from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from rest_framework import generics, mixins
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)
class UserLoginView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserLoginSerializer
    print("I'm here ")
    def get(self, request, *args, **kwargs):
        username = self.request.query_params.get('username', None)
        username = username.split("/")[0]
        print("username " +username)
        userID = User.objects.only('id').get(username=username).id
        return Response({'userid':userID}, status=HTTP_200_OK)