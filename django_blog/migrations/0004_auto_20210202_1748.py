# Generated by Django 3.1.6 on 2021-02-02 14:18

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_blog', '0003_auto_20210201_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_published',
            field=models.DateTimeField(blank=True, null=True, verbose_name='تاریخ انتشار'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_published',
            field=models.DateTimeField(blank=True, null=True, verbose_name='تاریخ انتشار'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='media/post_cover/', verbose_name='تصویر کاور'),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_active',
            field=models.BooleanField(verbose_name='فعال'),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(verbose_name='انتشار'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='django_blog.Tag', verbose_name='تگ ها'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='مطلب'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=20, verbose_name='عنوان مطلب'),
        ),
    ]