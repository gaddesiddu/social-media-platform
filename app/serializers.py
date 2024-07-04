from rest_framework import serializers
from .models import *
 

class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.IntegerField(source='followering.count', read_only=True)
    following_count = serializers.IntegerField(source='followers.count', read_only=True)
    class Meta:
        model = User
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.IntegerField(source='comments.count',read_only=True)
    likes_count = serializers.IntegerField(source='likes.count',read_only=True)
    class Meta:
        model = Post
        fields = ['id','user','content','image','created_at','comments','comments_count','likes_count']

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

