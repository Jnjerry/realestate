from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from auths.serializers import UserSerializer
from django.contrib.auth.models import User


class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
 
