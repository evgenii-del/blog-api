from rest_framework import serializers

from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for comments
    """

    author = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for posts
    """

    author = serializers.SlugRelatedField(slug_field="username", read_only=True)
    comments = CommentSerializer(many=True, required=False, read_only=True)
    votes = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = ("id", "title", "slug", "author", "comments", "votes", "created_at")
