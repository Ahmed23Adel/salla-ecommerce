from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import GenericUserSerializer, UserEmailActivation
from rest_framework.response import Response
from rest_framework  import generics
from .permissions import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings
from django.conf import settings
from rest_framework import generics
from .models import GenericUserData
from .models import *
from urllib.parse import urljoin
from .utils import *
from cryptography.fernet import Fernet


# Create your views here.
# view for registering users

class RegisterView(APIView):
    def post(self, request):
        user_serializer = GenericUserSerializer(data=request.data)
        
        if user_serializer.is_valid(raise_exception=True):
            user_serializer.save()
            email = request.data['email']
            first_name = request.data['first_name']
            send_verification_email(email, first_name, user_serializer.data)
            return Response(user_serializer.data)
        
        return Response(user_serializer.data)

class VerfiyUserAccount(generics.RetrieveAPIView):
    queryset = GenericUserData.objects.all()
    serializer_class = UserEmailActivation
    lookup_field ='id'
    
    def get(self, request, *args, **kwargs):
        self.kwargs[self.lookup_field]  = decode_verficiation_link(self.kwargs[self.lookup_field] )
        instace = self.get_object()
        instace.is_email_confirmed = True
        instace.save()
        return Response({"message": "Email was verified successfully"})
        





