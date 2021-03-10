from django.contrib.auth.models import AnonymousUser
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django_blog.models import (
    Post, Word
)
from django_blog.serializers import SearchedPostSerializer, CommentSerializer


class SearchPost(APIView):
    """
    List of all searched post (with get method)
    """

    def get(self, request, format=None):
        search_text = request.GET.get('search')
        if search_text:
            post_query_set = self.search_on_posts(search_text)
            return Response(SearchedPostSerializer(post_query_set, many=True).data,
                            status=status.HTTP_200_OK)
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def search_on_posts(self, text):
        posts_with_title = Post.objects.filter(title__icontains=text).all()
        posts_with_content = Post.objects.none()
        for word in Word.objects.filter(text__icontains=text).all():
            posts_with_content = posts_with_content | word.post_set.all()
        return (posts_with_content | posts_with_title).distinct()


class GetComment(generics.CreateAPIView):
    """
    """
    serializer_class = CommentSerializer
    permission_classes = []

    def perform_create(self, serializer):
        if not isinstance(self.request.user, AnonymousUser):
            serializer.save(author=self.request.user)
            # super().perform_create(serializer)
