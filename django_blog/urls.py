from django.contrib import admin
from django.urls import path

from django_blog import views

app_name = 'django_blog'
urlpatterns = [
    path('post/<int:pk>/', views.PostView.as_view(), name='post'),
    path('tag/<int:pk>/', views.TagPostsList.as_view(), name='tag'),
]