from celery import shared_task

from .models import Post


@shared_task
def hello():
    posts = Post.objects.all()
    for post in posts:
        post.votes.clear()
