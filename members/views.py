from .models import Members
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer, SignupSerializer
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView

class Login(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = auth.authenticate(
                request=request,
                username=serializer.data['username'],
                password=serializer.data['password']
            )
            if user is not None:
                auth.login(request, user)
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class Signup(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save(password = make_password(serializer.validated_data['password']))
            auth.login(request, new_user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class Logout(APIView):
    def post(self, request):
        auth.logout(request)
        return Response(status=status.HTTP_200_OK)