from django.contrib import admin
from django_blog.models import (
    Post, Tag, LikeComment, Comment, Category, LikePost
)


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    exclude = ('date_created', 'date_published')

    def get_form(self, request, obj=None, change=False, **kwargs):
        if not admin.ModelAdmin.has_change_permission(self, request):
            self.__class__.exclude = ('is_active', 'is_published', 'date_created', 'date_published')
        return super().get_form(request, obj, change, **kwargs)


# admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(LikeComment)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(LikePost)
