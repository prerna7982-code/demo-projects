from bson import ObjectId
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.
from .models import Posts
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from rest_framework import viewsets, status, generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

class AddPostapi(generics.CreateAPIView):
	authentication_classes = [JWTAuthentication]
	permission_classes = (IsAuthenticated,)
	parser_classes = (FormParser, MultiPartParser)
	queryset = Posts.objects.all()
	# permission_classes = ()
	serializer_class = PostCreateSerializer
	def post(self,request):
		comment=request.POST.get("comment").split(",")
		tags=request.POST.get("tags").split(",")
		username = request.POST.get("username")
		# user_details={"first_name":request.POST.get("first_name"),"last_name":request.POST.get("last_name")}
		post=Posts(post_title=request.POST.get("post_title"),post_description=request.POST.get("post_description"),comment=comment,tags=tags,username=username)
		post.save()
		# return HttpResponse("Inserted")
		# serializer = self.serializer_class(data=request.data)
		# serializer.is_valid(raise_exception=True)
		# serializer.save()

		return Response(data = {'status':'1',"message":"successfully created posts"})

class UpdatePost(generics.UpdateAPIView):
	authentication_classes = [JWTAuthentication]
	permission_classes = (IsAuthenticated,)
	parser_classes = (FormParser, MultiPartParser)
	# queryset = Posts.objects.all()
	serializer_class = PostCreateSerializer
	def post(self,request, *args,**kwargs):
		post=Posts.objects.get(post_title=self.kwargs['post_title'])
		post.comment=request.POST.get("comment").split(",")
		post.tags=request.POST.get("tags").split(",")
		post.username = request.POST.get("username")
		# post=Posts(post_title=request.POST.get("post_title"),post_description=request.POST.get("post_description"),comment=comment,tags=tags,username=username)
		post.save()
		return Response(data = {'status':'1',"message":"successfully updated posts"} )

class DeletePost(generics.GenericAPIView):
	# authentication_classes = []
	# permission_classes = (IsAuthenticated,)
	parser_classes = (FormParser, MultiPartParser)
	def get(self,request,post_title):
		post=Posts.objects.get(post_title=self.kwargs['post_title'])
		post.delete()
		return Response(data ={'message':"Post Deleted"})


class ListPosts(generics.ListAPIView):
	permission_classes = (AllowAny)
	queryset = Posts.objects.all()
	serializer_class = PostCreateSerializer


class DetailPost(generics.RetrieveAPIView):
	authentication_classes = [JWTAuthentication]
	permission_classes = (IsAuthenticated,)
	def get(self, request, *args,**kwargs):
		queryset = Posts.objects.get(post_title=self.kwargs['post_title'])
		d1 = queryset.post_title
		d2 = queryset.comment
		d3 =  queryset.username
		d4 = queryset.tags
		res = {"post_title":d1,"username":d3,"comment":d2,'tags':d4}
		return Response(data= res)