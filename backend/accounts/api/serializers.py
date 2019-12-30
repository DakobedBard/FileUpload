import datetime

from django.contrib.auth import get_user_model
from django.utils import timezone

from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse
from django.db.models import Q


User = get_user_model()

class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    email= serializers.EmailField(label="Email Address", required=False, allow_blank=True)
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'token',
            'id'
        ]
        extra_kwargs = {"password":{"write_only":True}}

    def validate(self, data):

        email = data["email"]
        password = data["password"]
        user = User.objects.filter(email=email).first()
        # If the user object is empty then it will trigger the exception.. not sure of a more elgeant solution this but
        # I'm sure that it exists...
        try:
            passw = user.password
        except Exception as e:
            raise serializers.ValidationError("User with that email address not found")
            return data

        if user.password != password:
             raise serializers.ValidationError("Incorrect Credentials")
        data['id'] = user.id
        return data

