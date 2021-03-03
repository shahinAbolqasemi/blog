from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django_blog.models import (
    Post, Tag, LikeComment, Comment, Category, LikePost, User, Word
)


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    exclude = ('date_created', 'date_published')

    def get_form(self, request, obj=None, change=False, **kwargs):
        if not admin.ModelAdmin.has_change_permission(self, request):
            self.__class__.exclude = ('is_active', 'is_published', 'date_created', 'date_published')
        return super().get_form(request, obj, change, **kwargs)

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)


class UserAdmin(BaseUserAdmin):
    fieldsets = tuple(('اطلاعات شخصی', {'fields': ('avatar', 'phone_number', 'first_name', 'last_name', 'email')})
                      if element == ('اطلاعات شخصی', {'fields': ('first_name', 'last_name', 'email')}) else element
                      for element in BaseUserAdmin.fieldsets)

    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {'fields': ('avatar', 'phone_number')}),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Tag)
admin.site.register(LikeComment)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(LikePost)
