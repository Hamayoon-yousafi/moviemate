from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .serializers import RegistrationSerializer
from .. import models


@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['response'] = 'Successfully registered'
            data['username'] = account.username
            data['email'] = account.email

            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors

        return Response(data)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=200)


# Doing the same but with class based view

# from .serializers import RegistrationSerializer
# from rest_framework import generics
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
# from rest_framework.response import Response


# class RegisterUser(generics.CreateAPIView):
#     serializer_class = RegistrationSerializer
#     queryset = User.objects.all()

#     def perform_create(self, serializer):
#         return serializer.save()
    
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         account = self.perform_create(serializer)
#         token = Token.objects.create(user=account)
#         return Response({'token': token.key})