from rest_framework import serializers
from .models import (
    Post, Tag, Comment
)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class SearchedPostSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    url = serializers.HyperlinkedIdentityField(view_name='django_blog:post')
    author = serializers.ReadOnlyField(source="author.username")
    category = serializers.ReadOnlyField(source="category.name")

    class Meta:
        model = Post
        fields = [
            'url',
            'title',
            'date_published',
            'tags',
            'author',
            'category',
            'description',
        ]


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Comment
        fields = [
            'text',
            'post',
            'author',
        ]
