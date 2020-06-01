from django.contrib.auth.models import User
from django.db import models
from autoslug import AutoSlugField


class Post(models.Model):
    """
    Post Model
    """

    title = models.CharField(max_length=150, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from="title", max_length=150, unique=True)
    votes = models.ManyToManyField(User, related_name="vote", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]


class Comment(models.Model):
    """
    Comment Model
    """

    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.post}: {self.content}"
