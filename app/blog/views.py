from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from rest_framework import viewsets


class PostViewSet(viewsets.ModelViewSet):
    """
    Create, read, update and delete a post
    """

    serializer_class = PostSerializer
    queryset = Post.objects.all().annotate(count_votes=Count("votes"))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action == "update" or self.action == "destroy":
            permission_classes = [IsOwnerOrReadOnly]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]


class CommentViewSet(viewsets.ModelViewSet):
    """
    Create, read, update and delete a comment
    """

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action == "update" or self.action == "destroy":
            permission_classes = [IsOwnerOrReadOnly]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]


class UpvoteView(APIView):
    """
    A view that allows the user to vote for a post
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        if post.votes.filter(id=self.request.user.id).exists():
            post.votes.remove(self.request.user)
            return Response(status=201)
        post.votes.add(self.request.user)
        return Response(status=201)
