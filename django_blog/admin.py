from django.contrib import admin
from django_blog.models import (
    Post, Tag, LikeComment, Comment, Category, LikePost
)

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(LikeComment)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(LikePost)
