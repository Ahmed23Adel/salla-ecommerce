from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from datetime import date
from uuid import uuid4
'''
Basically in the above code we created a class UserData which extends the UserManager class.
 The ‘username’ is set to be none because we want to authenticate the user by its unique email id instead of a username.

We have written ‘email’ in the USERNAME_NAME field which tells django that we want to input email id instead of username when authenticating.
'''
class UserManager(BaseUserManager):

    use_in_migration = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is Required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, password, **extra_fields)


class GenericUserData(AbstractUser):
    username = None
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_normal = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_emp = models.BooleanField(default=False)
    is_seller_activated = models.BooleanField(default=False)
    bdate = models.DateField(null=False)
    is_male = models.BooleanField(null=False)
    is_email_confirmed = models.BooleanField(default=False)
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name','is_normal', 'is_seller','is_emp','is_male','bdata']

    def __str__(self):
        return self.first_name + " "  + self.last_name
    

class EmailConfirmationToken(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(GenericUserData, on_delete=models.CASCADE)


class NormalSellerDetails(models.Model):
    userid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True,db_column='UserID', unique=True)  # from table user.
    mobileauthenticationenabled = models.IntegerField(db_column='MobileAuthenticationEnabled', default=0)  # Field name made lowercase.
    emailauthenticationenabled = models.IntegerField(db_column='EmailAuthenticationEnabled', default=0)  # Field name made lowercase.
    mobilephone = models.CharField(db_column='MobilePhone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    profilepiclink = models.CharField(db_column='ProfilePicLink', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'normalsellerdetails'


class Permissions(models.Model):
    empid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True,db_column='EmpID', unique=True)  # from table user.
    permissionkey = models.SmallIntegerField(db_column='PermissionKey')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'permissions'
        unique_together = (('empid', 'permissionkey'),)

