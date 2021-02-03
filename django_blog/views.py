from django.shortcuts import render
from django.views import generic
from .models import (
    Post
)


class PostView(generic.DetailView):
    model = Post
    template_name = 'django_blog/post.html'
