from django.shortcuts import render, get_object_or_404
from django.views import generic

from .forms import CommentModelForm
from .models import (
    Post, Tag
)


def index_view(request):
    return render(request, 'django_blog/index.html', {'posts': Post.objects.filter(is_published=True)})


class PostView(generic.DetailView):
    model = Post
    template_name = 'django_blog/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            print(self.request)
            comment_form = CommentModelForm(data=self.request.POST)
            comment_form.cleaned_data['post'] = context['post']
        else:
            context['comment_form'] = CommentModelForm(prefix='comment')
        return context


class TagPostsList(generic.ListView):
    template_name = 'django_blog/tag_posts.html'
    context_object_name = 'posts'
    extra_context = {}

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, id=self.kwargs['pk'])
        self.extra_context['tag'] = self.tag
        return self.tag.post_set.all()
