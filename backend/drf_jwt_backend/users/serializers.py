from distutils.log import Log
from rest_framework import serializers
from .models import User, Photo, Comment, Log

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'first_name',
                  'last_name',
                  'city',
                  'state',
                  'email',
                  'experiences',
                  'interests',
                  'created_on',)
        
class AbuseLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ('incidenttype',
                  'username',
                  'description',
                  'comment',
                  'state',
                  'image',
                  'created_on')
        
class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('imagefield',
                  'created_on'
                  )
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user',
                  'photo',
                  'content',
                  'date_created',
                  'ordering')
