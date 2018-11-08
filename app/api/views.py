from django.shortcuts import render
from blog.serializers import ArticleSerializer
from blog.models import Article
from rest_framework import generics


# Create your views here.
class ListArticleView(generics.ListAPIView):
    """
    Provides a get method handler to fetch an article.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

# Create your views here.
class GetArticleView(generics.RetrieveAPIView):
    """
    Provides a get method handler to fetch an article.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'machine_name'
    lookup_url_kwarg = 'id'