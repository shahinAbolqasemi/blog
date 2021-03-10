from django_blog.models import Category
from django_blog.utils.utils import get_categories_dict


def categories(request):
    return {'posts_categories': get_categories_dict(Category.objects.all())}
