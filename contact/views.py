from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.generics import (
    CreateAPIView,
)
from rest_framework import status
from django.contrib.auth import authenticate

# Local Import her
from .serializers import (
    # UserSerializer,
    ContactUsSerializer,
    UserDataSerializer,
    UserCreateSerializer,
    UserLoginSerializer
)

from .models import ContactUs

'''
Signup api.
'''


# class UserCreate(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         token, created = Token.objects.get_or_create(user=serializer.instance)
#         return Response({'token': token.key, 'user': str(serializer.instance)},
#                         headers=headers,
#                         status=status.HTTP_201_CREATED)


'''
ContactUs api view.
'''


class ContactUsAPIView(CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


'''
    Register View
'''


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDataSerializer

    def post(self, request):
        user = UserCreateSerializer(data=request.data)

        if user.is_valid():
            userInstance = user.save()
            token = Token.objects.create(user=userInstance)
            userInstance = UserDataSerializer(userInstance).data

            return Response({
                'user': userInstance,
                'token': token.key
            }, status=status.HTTP_201_CREATED)

        return Response({
            'detail': user.errors
        }, status=status.HTTP_400_BAD_REQUEST)


'''
Login Api
'''


class LoginView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({
                'detail': 'User not found.'
            }, status=status.HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        user = UserDataSerializer(user).data
        return Response({
            'user': user,
            'token': token.key
        }, status=status.HTTP_200_OK)
