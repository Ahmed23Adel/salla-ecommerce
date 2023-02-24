from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import GenericUserSerializer
from rest_framework.response import Response
from rest_framework  import generics
from .permissions import *
from rest_framework_simplejwt.authentication import JWTAuthentication

