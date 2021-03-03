from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "my help desc"

    def add_arguments(self, parser):
        parser.add_argument('group', type=str)
        parser.add_argument('-p', '--permissions', nargs='+', default=None)

    def handle(self, *args, **options):
        try:
            group = Group.objects.get(name=options['group'])
        except Group.DoesNotExist:
            self.stdout.write("- Group that was entered doesn't exist. Do you want create it?(yes/no)", ending=' ')
            if input().lower() == 'yes':
                group = Group.objects.create(name=options['group'])
                self.stdout.write("- Group created successfully!!!")
            else:
                exit()
        if options['permissions']:
            for permission in options['permissions']:
                try:
                    perm = Permission.objects.get(codename=permission)
                except Permission.DoesNotExist as ex:
                    raise CommandError("- Permissions that was entered doesn't exist.\n"
                                       "- hint: for enter permissions codename use -p codename, -permissions codename.\n"
                                       "- hint: permission codename sections shouldn't be separated by space"
                                       "should be separated by underscore.")
                group.permissions.add(perm)
                self.stdout.write(self.style.SUCCESS('- Successfully added permission "%s" to group %s.'
                                                     % (perm.name, group.name)))
