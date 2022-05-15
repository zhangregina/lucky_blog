from rest_framework import generics
from rest_framework.response import Response
from .serializers import *
from rest_framework.authtoken.views import ObtainAuthToken


class BlogerSignUpView(generics.GenericAPIView):
    serializer_class = BlogerSignUpSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": Token.objects.get(user=user).key,
            "message": "The user is created."
        })


class ReaderSignUpView(generics.GenericAPIView):
    serializer_class = ReaderSignUpSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": Token.objects.get(user=user).key,
            "message": "The user is created."
        })


class CustomAuthTokenView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'username': user.username,
            'token': token.key,
            'user_id': user.pk,
            'is_reader': user.is_reader
        })