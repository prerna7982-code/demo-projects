from django.contrib.auth import get_user_model, password_validation
# from rest_framework.authtoken.models import Token
from rest_framework import serializers
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.password_validation import validate_password
from django.core.validators import RegexValidator
import os
from rest_framework.exceptions import AuthenticationFailed
from .models import CustomUser

from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .utils import *
User = get_user_model()
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username

        return token

class UserLoginSerializer(serializers.Serializer):
    access_token = serializers.CharField(max_length=255, required=True)
    username = serializers.CharField(max_length=255, required=True)
    email = serializers.CharField(max_length=255, required=False)
    password = serializers.CharField(required=True, write_only=True)
    def validate(self, attrs):
        self.token = attrs['access_token']
        self.res = setRedis("access_token",self.token,43200)
        return attrs

class AuthUserSerializer(serializers.ModelSerializer):

	class Meta:
		 model = CustomUser
		 fields = ('id','username','email','first_name', 'last_name','avatar','is_active')
		 read_only_fields = ('id', 'is_active', 'is_staff')
	

class EmptySerializer(serializers.Serializer):
	pass


class UserRegisterSerializer(serializers.ModelSerializer):
	"""
	A CustomUser serializer for registering the CustomUser
	"""
	class Meta:
		model = CustomUser
		fields = ('id','username','email','first_name', 'last_name','avatar','password')

	def validate_CustomUsername(self, value):
	    user = CustomUser.objects.filter(Username='Username')
	    if user:
	        raise serializers.ValidationError("Username is already taken")
	    return value
	# def validate_phone(self, value):
	#     CustomUser = CustomUser.objects.filter(phone='phone')
	#     if CustomUser:
	#         raise serializers.ValidationError("CustomUsername with this phone number is already taken")
	#     return value
	def validate_email(self, value):
		user = CustomUser.objects.filter(email='email')
		if user:
			raise serializers.ValidationError("Username with this email is already taken")
		return BaseUserManager.normalize_email(value)

	def validate_password(self, value):
		password_validation.validate_password(value)
		return value

	def create(self, validated_data):
		
		user = User(**validated_data)
		user.set_password(validated_data['password'])
		user.save()        
		return user

class UpdateCustomUserSerializer(serializers.ModelSerializer):

	class Meta:
		model = CustomUser
		fields = ('email','first_name', 'last_name','avatar')

	def validate_email(self, value):
		user = self.context['request'].user
		if user.objects.exclude(pk=user.pk).filter(email=value).exists():
			raise serializers.ValidationError({"email": "This email is already in use."})
		return value

	def validate_username(self, value):
	    user = self.context['request'].user
	    if user.objects.exclude(pk=user.pk).filter(username=value).exists():
	        raise serializers.ValidationError({"username": "This username is already in use."})
	    return value
	# def validate_phone(self, value):
	#     CustomUser = self.context['request'].CustomUser
	#     if CustomUser.objects.exclude(pk=CustomUser.pk).filter(phone=value).exists():
	#         raise serializers.ValidationError({"phone:  This phone number is already in use"})
		# return value

	def update(self, instance, validated_data):
		instance.email = validated_data['email']
		instance.first_name = validated_data['first_name']
		instance.last_name = validated_data['last_name']
		instance.avatar = validated_data['avatar']       
		instance.save()

		return instance




class LogoutSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    def validate(self, attrs):
        self.token = attrs['access_token']
        return attrs

    # def save(self, **kwargs):
    #     try:
    #         RefreshToken(self.token).blacklist()
    #     except:
    #         raise serializers.ValidationError("Bad token")
    def delete(self, **kwargs):
    	try:
    		res = setExpiry(self.token)
    	except:
    		raise serializers.ValidationError("Bad token")
