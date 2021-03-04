from django.db.models.signals import (
    pre_save, post_save
)
from django.dispatch import receiver
from django.utils import timezone

from .utils.persian_text_tools import tokenize_text, remove_html_tags, detect_lang
from .utils.stopwords.stopwords import PERSIAN_STOPWORDS
from django_blog.models import Post, Word, Comment
from django.db import transaction


@receiver(pre_save, sender=Post)
def post_pre_save(sender, instance, *args, **kwargs):
    # set date to publish a post
    set_date_of_published(instance)


@receiver(post_save, sender=Post)
def post_post_save(sender, instance, created, *args, **kwargs):
    # add content words to Word table
    transaction.on_commit(lambda: save_content_words_after_post_model_transaction(instance))


@receiver(pre_save, sender=Comment)
def comment_post_save(sender, instance, created, *args, **kwargs):
    # set date to publish a comment
    set_date_of_published(instance)


def save_content_words_after_post_model_transaction(instance):
    content = remove_html_tags(instance.content)
    for word in tokenize_text(content):
        if word not in PERSIAN_STOPWORDS:
            language = detect_lang(word)
            word_instance, _ = Word.objects.update_or_create(text=word, lang=language)
            instance.content_words.add(word_instance)


def set_date_of_published(instance):
    if instance.is_published:
        instance.date_published = timezone.now()
