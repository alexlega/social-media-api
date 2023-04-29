from rest_framework import viewsets

from .models import Profile, Post
from .permissions import IsAdminOrIfAuthenticatedReadOnly
from .serializers import (
    ProfileSerializer,
    ProfileDetailSerializer,
    PostSerializer
)
from user.models import User
from user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        email = self.request.query_params.get("email")

        queryset = self.queryset

        if email:
            queryset = queryset.filter(email__icontains=email)

        return queryset.distinct()


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ["retrieve", "update", "create"]:
            return ProfileDetailSerializer

        return self.serializer_class

    def get_queryset(self):
        username = self.request.query_params.get("username")
        first_name = self.request.query_params.get("first_name")
        last_name = self.request.query_params.get("last_name")

        queryset = self.queryset

        if username:
            queryset = queryset.filter(nickname__icontains=username)

        if first_name:
            queryset = queryset.filter(first_name__icontains=first_name)

        if last_name:
            queryset = queryset.filter(last_name__icontains=last_name)

        return queryset


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        tag = self.request.query_params.get("hashtag")

        queryset = self.queryset

        if tag:
            queryset = queryset.filter(hashtag__icontains=tag)

        return queryset
