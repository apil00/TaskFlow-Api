from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password']

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError('user already exists with email.')
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser.objects.create_user(
            password=password,
            **validated_data
        )
        return user

class LoginSerializer(serializers.serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if not email and not password:
            raise serializers.ValidationError("Email and Password are required.")

        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError("Invalid Credentials.")

        data['user']=user
        return data