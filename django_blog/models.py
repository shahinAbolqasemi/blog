from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField('عنوان', max_length=20)
    text = models.TextField('متن')
    image = models.URLField('تصویر')
    is_active = models.BooleanField('وضعیت')
    is_published = models.BooleanField('وضعیت انتشار')
    date_created = models.DateTimeField('تاریخ ثبت')
    date_published = models.DateTimeField('تاریخ انتشار')
    tags = models.ManyToManyField('Tag')
    author = models.ForeignKey('نویسنده', User, on_delete=models.CASCADE)
    category = models.ForeignKey('دسته بندی', 'Category', on_delete=models.CASCADE)
    likes = models.ManyToManyField(
        User,
        through='LikePost',
        through_fields=('post', 'user')
    )

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField('نام')

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.CharField('متن', max_length=200)
    is_published = models.BooleanField('وضعیت انتشار')
    date_create = models.DateTimeField('تاریخ ثبت')
    date_published = models.DateTimeField('تاریخ انتشار')
    post = models.ForeignKey('مطلب', Post, on_delete=models.CASCADE)
    author = models.ForeignKey('نویسنده', User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(
        User,
        through='LikeComment',
        through_fields=('post', 'author')
    )

    def __str__(self):
        return self.text[:50] + '...'


class LikePost(models.Model):
    is_liked = models.BooleanField('وضعیت پسندیدن')
    post = models.ForeignKey('مطلب', Post, on_delete=models.CASCADE)
    author = models.ForeignKey('نظر دهنده', User, on_delete=models.CASCADE)

    def __str__(self):
        return self.is_liked


class Category(models.Model):
    name = models.CharField('نام', max_length=20)

    def __str__(self):
        return self.name


class LikeComment(models.Model):
    is_liked = models.BooleanField('وضعیت پسندیدن')
    comment = models.ForeignKey('نظر', Comment, on_delete=models.CASCADE)
    author = models.ForeignKey('نویسنده', User, on_delete=models.CASCADE)

    def __str__(self):
        return self.is_liked
