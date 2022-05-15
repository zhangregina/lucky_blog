from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_reader']


class BlogerSignUpSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise ValidationError({"error": 'Passwords do not match!'})
        user.set_password(password)
        user.is_bloger = True
        user.save()
        Bloger.objects.create(user=user)
        return user


class ReaderSignUpSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise ValidationError({"error": 'Passwords do not match'})
        user.set_password(password)
        user.is_reader = True
        user.save()
        Reader.objects.create(user=user)
        return user
