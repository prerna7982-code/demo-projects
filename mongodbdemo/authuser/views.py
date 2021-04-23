from django.core.exceptions import ImproperlyConfigured
from rest_framework import viewsets, status, generics
from rest_framework.views import APIView
# from rest_framework.decorators import action
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import CustomUser
# from .utils import *
from django.contrib.auth import get_user_model, logout, login
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
# from twilio.rest import Client
from .serializers import *
# from .exception_handling import *
import random
# import redis
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.authentication import BasicAuthentication
# from rest_framework_simplejwt.token_blacklist.models import OutstandingToken,BlacklistedToken
# from drf_yasg.utils import swagger_auto_schema
from urllib.error import HTTPError

# CustomUser = get_CustomUser_model()

class RegisterView(generics.CreateAPIView):
	authentication_classes = [BasicAuthentication]
	parser_classes = (FormParser, MultiPartParser)
	queryset = CustomUser.objects.all()
	permission_classes = (IsAuthenticated,)
	serializer_class = UserRegisterSerializer


class UpdateProfileView(generics.UpdateAPIView):
	authentication_classes = [JWTAuthentication]
	parser_classes = (FormParser, MultiPartParser)
	queryset = CustomUser.objects.all()
	permission_classes = (IsAuthenticated,)
	serializer_class = UpdateCustomUserSerializer

class MyObtainTokenPairView(TokenObtainPairView):
	authentication_classes = [BasicAuthentication]
	parser_classes = (FormParser, MultiPartParser)
	permission_classes = (IsAuthenticated,)
	serializer_class = MyTokenObtainPairSerializer

class LoginApiView(generics.GenericAPIView):
	# authentication_classes = [JWTAuthentication]
	parser_classes = (FormParser, MultiPartParser)
	# permission_classes = (IsAuthenticated,)
	serializer_class = UserLoginSerializer
	def post(self,request):
		serializer = self.serializer_class(data=request.data)
		serializer.is_valid(raise_exception=True)
		# serializer.save()

		return Response(data = {'status':'1',"message":"successfully logged in"})


class UserDetailView(generics.ListAPIView):
	authentication_classes = [JWTAuthentication]
	parser_classes = (FormParser, MultiPartParser)
	queryset = CustomUser.objects.all()
	permission_classes = (IsAuthenticated,)
	serializer_class = AuthUserSerializer


class UserLogout(generics.GenericAPIView):
	authentication_classes = [JWTAuthentication]
	parser_classes = (FormParser, MultiPartParser)
	permission_classes = (IsAuthenticated,)
	serializer_class = LogoutSerializer

	def post(self,request):
		serializer = self.serializer_class(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()

		return Response(data = {"status":"1","message":"successfully logged out"})


class UserLogout(generics.GenericAPIView):
	# authentication_classes = [JWTAuthentication]
	# parser_classes = (FormParser, MultiPartParser)
	# permission_classes = (IsAuthenticated,)
	serializer_class = LogoutSerializer

	def post(self,request):
		# logouttoken = request.POST.get("token")
		# res = setExpiry(logouttoken)
		serializer = self.serializer_class(data=request.data)
		serializer.is_valid(raise_exception=True)
		# serializer.save()

		return Response(data = {"status":"1","message":"successfully logged out"})