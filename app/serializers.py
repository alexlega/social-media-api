from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user_author', 'content', 'created_at')


class PostListSerializer(PostSerializer):
    user_author = serializers.CharField(source="user_author.username", read_only=True)


class PostDetailSerializer(PostSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    user_first_name = serializers.CharField(source="user_profile.first_name", read_only=True)
    user_last_name = serializers.CharField(source="user_profile.last_name", read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'username', 'first_name', "last_name", 'content', 'created_at')
