from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import GenericUserSerializer, UserEmailActivation, AccountNormalSerializer
from .serializers import *
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
from django.db.models import Prefetch
from django.db.models import Case, When, BooleanField,F
from django.db.models import BooleanField, ExpressionWrapper, Q
from datetime import date,timedelta
from django.db.models import F, Value
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
    
class UserBanView(generics.ListCreateAPIView):
    queryset = UserBan.objects.all()
    serializer_class = UserBanSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmpBan]


class NormalAccountList(generics.ListCreateAPIView):
    serializer_class = AccountNormalSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmpReadAllUsersOrPost]

    def get_queryset(self):
        #queryset = NormalSellerDetails.objects.all().select_related('userid')
        datetime_now = str(date.today())
        queryset =  NormalSellerDetails.objects.select_related(
                    'user', 'user__userban').all().annotate(
                    is_banned_now=Case(
                        When(user__userban__isnull=False ,user__userban__to_date__gt=datetime_now, then=True),
                        default=False,
                        output_field=BooleanField()
                    )
                ).filter(user__is_normal=True)
        return queryset
    

class SellerAccountList(generics.ListCreateAPIView):
    serializer_class = AccountNormalSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmpReadAllUsersOrPost]

    def get_queryset(self):
        #queryset = NormalSellerDetails.objects.all().select_related('userid')
        datetime_now = str(date.today())
        queryset =  NormalSellerDetails.objects.select_related(
                    'user', 'user__userban').all().annotate(
                    is_banned_now=Case(
                        When(user__userban__isnull=False ,user__userban__to_date__gt=datetime_now, then=True),
                        default=False,
                        output_field=BooleanField()
                    )
                ).filter(user__is_seller=True)
        return queryset




class NormalAccountInsert(generics.CreateAPIView):
    queryset = NormalSellerDetails.objects.all()
    serializer_class= AccountNrmlSlrInsertSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsInsertUpdateNormalSelf]
    lookup_field = 'pk'

class SellerAccountInsert(generics.CreateAPIView):
    queryset = NormalSellerDetails.objects.all()
    serializer_class= AccountNrmlSlrInsertSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsInsertUpdateSellerSelf]
    lookup_field = 'pk'



class NormalAccountUpdate(generics.UpdateAPIView):
    queryset = NormalSellerDetails.objects.all()
    serializer_class= AccountNrmlSlrUpdateSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsInsertUpdateNormalSelf]


    def get_object(self):
        """
        I take the id of what I'm looking for from request.user
        So user can update the user who he is signed in only        
        """
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(pk=self.request.user.id)
        self.check_object_permissions(self.request, obj)
        return obj
    

class SellerAccountUpdate(generics.UpdateAPIView):
    queryset = NormalSellerDetails.objects.all()
    serializer_class= AccountNrmlSlrUpdateSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsInsertUpdateSellerSelf]


    def get_object(self):
        """
        I take the id of what I'm looking for from request.user
        So user can update the user who he is signed in only        
        """
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(pk=self.request.user.id)
        self.check_object_permissions(self.request, obj)
        return obj

