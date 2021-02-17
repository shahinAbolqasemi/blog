from django.forms import ModelForm

from django_blog.models import Comment


class CommentModelForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

