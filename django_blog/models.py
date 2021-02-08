from ckeditor.fields import RichTextField
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatar', verbose_name='آواتار', blank=True, null=True)
    phone_number = PhoneNumberField(max_length=30, blank=True, null=True, verbose_name='شماره تلفن')


class Category(models.Model):
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    name = models.CharField('نام', max_length=100)
    sup_category = models.ForeignKey(verbose_name='دسته بندی پدر', to='Category', on_delete=models.CASCADE,
                                     blank=True, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        verbose_name = 'مطلب'
        verbose_name_plural = 'مطلب ها'

    title = models.CharField('عنوان مطلب', max_length=150)
    content = RichTextField('مطلب')
    cover = models.ImageField('تصویر کاور', upload_to='post_cover')
    is_active = models.BooleanField('فعال', default=True)
    is_published = models.BooleanField('انتشار', default=False)
    date_created = models.DateTimeField('تاریخ ثبت', default=timezone.now)
    date_published = models.DateTimeField('تاریخ انتشار', blank=True, null=True)
    tags = models.ManyToManyField(verbose_name='تگ ها', to='Tag', blank=True)
    author = models.ForeignKey(verbose_name='نویسنده', to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(verbose_name='دسته بندی', to=Category, on_delete=models.CASCADE)
    users_who_liked = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='LikePost',
        through_fields=('post', 'author'),
        related_name='post_likes',
    )

    def __str__(self):
        return self.title


class Tag(models.Model):
    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'

    name = models.CharField('نام', max_length=100)

    def __str__(self):
        return self.name


class Comment(models.Model):
    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    text = models.CharField('متن', max_length=350)
    is_published = models.BooleanField('وضعیت انتشار', default=False)
    date_create = models.DateTimeField('تاریخ ثبت', default=timezone.now)
    date_published = models.DateTimeField('تاریخ انتشار', blank=True, null=True)
    post = models.ForeignKey(verbose_name='مطلب', to=Post, on_delete=models.CASCADE)
    author = models.ForeignKey(verbose_name='نویسنده', to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    users_who_liked = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='LikeComment',
        through_fields=('comment', 'author'),
        related_name='comment_likes',
    )

    def __str__(self):
        return self.text[:50] + '...'


class LikePost(models.Model):
    class Meta:
        verbose_name = 'پسندیدن مطلب'
        verbose_name_plural = 'پسندیدن مطالب'

    is_liked = models.BooleanField('وضعیت پسندیدن')
    post = models.ForeignKey(verbose_name='مطلب', to=Post, on_delete=models.CASCADE)
    author = models.ForeignKey(verbose_name='نظر دهنده', to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.is_liked


class LikeComment(models.Model):
    class Meta:
        verbose_name = 'پسندیدن نظر'
        verbose_name_plural = 'پسندیدن نظرات'

    is_liked = models.BooleanField('وضعیت پسندیدن')
    comment = models.ForeignKey(verbose_name='نظر', to=Comment, on_delete=models.CASCADE)
    author = models.ForeignKey(verbose_name='نویسنده', to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.is_liked
