# Generated by Django 3.1.6 on 2021-02-02 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_blog', '0004_auto_20210202_1748'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='cover',
        ),
    ]