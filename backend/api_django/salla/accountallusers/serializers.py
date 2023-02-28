from .models import GenericUserData, NormalSellerDetails
from .models import *
from rest_framework import serializers
from password_strength import PasswordPolicy
from datetime import date

class GenericUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = GenericUserData    
        fields = ["id", "email", "first_name", 'last_name', "password", 'is_seller', 'is_normal', 'is_emp', 'is_male', 'bdate']

    def create(self, validated_data):
        user = GenericUserData.objects.create(email=validated_data['email'],
                                first_name=validated_data['first_name'],
                                last_name=validated_data['last_name'],
                                is_seller = validated_data['is_seller'],
                                is_normal = validated_data['is_normal'],
                                is_emp = validated_data['is_emp'],
                                bdate = validated_data['bdate'],
                                is_male = validated_data['is_male'],
                                )
        
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def has_numbers(self,string):
        return any(char.isdigit() for char in string)


    def validate(self, attrs):
        policy = PasswordPolicy.from_names(
            length=8,  # min length: 8
            uppercase=2,  # need min. 2 uppercase letters
            numbers=2,  # need min. 2 digits
            special=2,  # need min. 2 special characters
            nonletters=2,  # need min. 2 non-letter characters (digits, specials, anything)
        )
        password_op = policy.test(attrs['password'])
        if not len(password_op)  == 0:
            raise serializers.ValidationError(f"Password strengh check has failed, some checks have failed, which are {str(password_op)}")
        if attrs['is_seller'] and attrs['is_normal'] :
            raise serializers.ValidationError("You can't be serller and normal user at the same time.")
        if self.has_numbers(attrs['first_name']) or  self.has_numbers(attrs['last_name']):
            raise serializers.ValidationError("You must insert first and last name.")
        if attrs['is_emp']:
            raise serializers.ValidationError("You don't have the permission to create an employee.")
        return attrs
        # TODO make user login and make sure that he is an employee who has permission to insert another emp and then allow him



class UserEmailActivation(serializers.ModelSerializer):
    class Meta:
        model = GenericUserData
        fields = ['is_email_verified']
    

class UserBanSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBan
        fields = ['user_id', 'from_date','to_date']


class GenericUserRetrievalSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenericUserData    
        fields = [ "email", "first_name", 'last_name', 'is_seller', 'is_normal', 'is_emp', 'is_male', 'bdate']

class AccountNormalSerializer(serializers.ModelSerializer):
    # for list update
    user = GenericUserRetrievalSerializer(many=False)
    is_banned_now = serializers.BooleanField(
        read_only=True)
    class Meta:
        model = NormalSellerDetails
        fields = ['mobileauthenticationenabled',
                'emailauthenticationenabled',
                'mobilephone',
                'profilepiclink',
                'user',
                'is_banned_now'
                ]

    
class AccountNrmlSlrInsertSerializer(serializers.ModelSerializer):
    class Meta:
        model = NormalSellerDetails
        fields = [
                'mobileauthenticationenabled',
                'emailauthenticationenabled',
                'mobilephone',
                'profilepiclink',
                'user',
        ]



class AccountNrmlSlrUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NormalSellerDetails
        fields = [
                'mobileauthenticationenabled',
                'emailauthenticationenabled',
                'mobilephone',
                'profilepiclink',
        ]


    