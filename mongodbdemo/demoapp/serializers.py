from rest_framework import serializers
from .models import Posts
class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
         model = Posts
         fields = ('post_title','post_description','comment','tags','username')
         read_only_field = ('_id')
    