from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    related_word = models.CharField(max_length=14, unique=True)


class Profile(models.Model):
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    username = models.CharField(max_length=23)
    first_name = models.CharField(max_length=23)
    last_name = models.CharField(max_length=23)
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="following",
        blank=True
    )

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return f"{self.username} ({self.full_name})"


class Post(models.Model):
    user_author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    content = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name="posts", blank=True)

    class Meta:
        ordering = ['-created_at']

    def posts_preview(self):
        return self.content[:20]

    def __str__(self):
        return f"{self.user_author.username} - {self.content}"
