from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import GenericUserSerializer
from rest_framework.response import Response
from rest_framework  import generics
from .permissions import *
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from dotenv import load_dotenv
from django.conf import settings

load_dotenv()


class cusomt_permission(permissions.BasePermission):

    def is_emp_has_all_perms(self,user):
        return self.has_user_perm(user, settings.EMP_ALL_PERMISSIONS)
    
    def has_user_perm(self, user, perm):
        return len(user.permissions_set.all().filter(permissionkey = perm)) >= 1

class IsEmpReadAllUsersOrPost(cusomt_permission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method == "GET":
                if request.user.is_emp and (self.is_emp_has_all_perms(request.user) \
                                            or self.has_user_perm(request.user,settings.EMP_NRMLSLR_VIEW)):
                    return True
            if request.method == "POST":
                return True
            return False

    def has_object_permission(self, request, view, obj):
        return False
    


class IsEmpBan(cusomt_permission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
                if request.user.is_emp and (self.is_emp_has_all_perms(request.user) \
                                            or self.has_user_perm(request.user,settings.EMP_BAN_USER)):
                    return True
                return False

    def has_object_permission(self, request, view, obj):
        return False
    

class IsInsertNormalSelf(cusomt_permission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method == "POST":
                if request.user.is_normal and str(request.user.id).replace("-", "")== request.data.get('user'):            
                    return True
            elif request.method == "PUT": 
                if request.user.is_normal :   
                    return True

        return False
        

    def has_object_permission(self, request, view, obj):
        if request.user.is_normal : 
            return True
        return False
    