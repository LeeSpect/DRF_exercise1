from dj_rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from rest_framework import serializers
from .models import Members

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(max_length=100)
    email = serializers.EmailField(required=True)
    location = serializers.CharField(max_length=100)
    university = serializers.CharField(max_length=100)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'location': self.validated_data.get('location', ''),
            'university': self.validated_data.get('university', ''),
        }
        
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.username = self.cleaned_data.get('username')
        user.nickname = self.cleaned_data.get('nickname')
        user.email = self.cleaned_data.get('email')
        user.location = self.cleaned_data.get('location')
        user.university = self.cleaned_data.get('university')
        user.save()
        adapter.save_user(request, user, self)
        return user
    
class CustomUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ['id', 'username', 'password', 'nickname', 'email', 'locatoin', 'university']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=120)
    
class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ['username', 'password', 'nickname', 'email', 'location', 'university']