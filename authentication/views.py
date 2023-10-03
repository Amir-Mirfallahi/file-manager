from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import *
from rest_framework.response import Response

from .serializers import UserSerializer
from rest_framework.permissions import *


class UserRegistrationApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserListApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class SingleUserApiView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CheckUsernameView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        username = self.request.query_params.get('username')
        email = self.request.query_params.get('email')
        if username:
            return User.objects.filter(username=username)
        elif email:
            return User.objects.filter(email=email)
        return User.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            return Response({'exists': True}, status=status.HTTP_200_OK)
        return Response({'exists': False}, status=status.HTTP_200_OK)
