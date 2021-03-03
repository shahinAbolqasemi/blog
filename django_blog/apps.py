from django.apps import AppConfig


class DjangoBlogConfig(AppConfig):
    name = 'django_blog'

    def ready(self):
        import django_blog.signals
