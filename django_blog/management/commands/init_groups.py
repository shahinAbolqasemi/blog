from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = ""
    GROUPS_NAME_WITH_PERMISSIONS = {
        'simple': [
            'view_post',
            'view_comment',
            'view_category',
            'view_tag',
            'search_posts',
            'add_comment',
            'like_post',
            'like_comment',
        ],
        'author': [
            'view_post',
            'view_comment',
            'view_category',
            'view_tag',
            'search_posts',
            'add_comment',
            'like_post',
            'like_comment',
            'add_post',
            'change_self_post',
        ],
        'editor': [
            'view_post',
            'view_comment',
            'view_category',
            'view_tag',
            'search_posts',
            'add_comment',
            'like_post',
            'like_comment',
            'add_post',
            'change_post',
            'confirm_posts',
            'confirm_comments',
        ],
        'admin': [
            'view_post',
            'view_comment',
            'view_category',
            'view_tag',
            'search_posts',
            'add_comment',
            'like_post',
            'like_comment',
            'add_post',
            'change_post',
            'confirm_posts',
            'confirm_comments',
            'add_category',
            'change_category',
            'delete_category',
            'view_user',
            'add_user',
            'change_user',
            'delete_user',
        ],
    }

    def handle(self, *args, **options):
        for group_name in self.GROUPS_NAME_WITH_PERMISSIONS:
            group, created = Group.objects.update_or_create(name=group_name)
            self.stdout.write(self.style.SUCCESS('- Successfully added group %s:' % group_name))
            for permission_codename in self.GROUPS_NAME_WITH_PERMISSIONS[group_name]:
                try:
                    permission = Permission.objects.get(codename=permission_codename)
                    self.stdout.write(self.style.SUCCESS(
                        '\t- Successfully added permission %s to group %s' % (permission_codename, group_name)))
                except Permission.DoesNotExist as ex:
                    raise CommandError("- Permissions %s doesn't exist." % permission_codename)
                group.permissions.add(permission)
        self.stdout.write(self.style.SUCCESS('- Successfully groups created and its permissions added.'))
