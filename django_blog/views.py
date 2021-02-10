from django.shortcuts import render
from django.views import generic
from .models import (
    Post
)


def index_view(request):
    return render(request, 'django_blog/index.html', {'posts': Post.objects.all()})


class PostView(generic.DetailView):
    model = Post
    template_name = 'django_blog/post.html'
