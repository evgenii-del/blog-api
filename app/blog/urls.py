from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import PostViewSet, CommentViewSet, UpvoteView

posts = PostViewSet.as_view({"get": "list", "post": "create"})

posts_detail = PostViewSet.as_view({"put": "update", "delete": "destroy"})

comments = CommentViewSet.as_view({"post": "create"})

comments_detail = CommentViewSet.as_view({"put": "update", "delete": "destroy"})

urlpatterns = format_suffix_patterns(
    [
        path("posts/", posts),
        path("posts/<int:pk>/", posts_detail),
        path("comments/", comments),
        path("comments/<int:pk>/", comments_detail),
        path("posts/<int:pk>/upvotes/", UpvoteView.as_view()),
    ]
)
