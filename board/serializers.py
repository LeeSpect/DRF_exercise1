from rest_framework import serializers
from .models import *


class BoardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'user', 'title', 'body']
        read_only_fields = ['user']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'created_at', 'comment']
        read_only_fields = ['user']
        
        
class BoardSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Board
        fields = ['id', 'user', 'title', 'body', 'comments']
        read_only_fields = ['user']