from rest_framework import serializers

from .models import Profile, Post
from user.serializers import UserSerializer


class ProfileSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = (
            "id",
            "username",
            "full_name",
            "followers",
        )

    def get_followers_count(self, obj):
        return obj.user.following.count()


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "user_author",
            "profile",
            "content",
            "created_at",
            "tag"
        )
        read_only_fields = ["author", ]


class ProfileDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    posts = PostSerializer(many=True, read_only=True)
    following = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            "username",
            "first_name",
            "last_name",
            "posts",
            "following",
            "followers"
        )

    def get_following(self, obj):
        return [follower.username for follower in obj.followers.all()]

    def get_followers(self, obj):
        return [
            followed_user.user.username for followed_user in obj.user.following.all()
        ]
