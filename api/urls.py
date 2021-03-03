from django.contrib import admin
from django.urls import path
from .views import (
    SearchPost, GetComment
)

app_name = 'api'
urlpatterns = [
    path('search', SearchPost.as_view(), name='simple_search'),
    path('comment/add', GetComment.as_view(), name='getComment'),
]
