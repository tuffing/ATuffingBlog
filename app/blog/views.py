from django.shortcuts import get_object_or_404, render 

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .serializers import ArticleSerializer

from .models import Article

def index(request):
    latest = Article.objects.order_by('-pub_date')[:1].get()
    latest_articles = sidebar()
    
    context = { 'article': latest, 'latest_articles': latest_articles}
    return render(request, 'blog/index.html', context)

def article(request, article_machine_name):
    article = get_object_or_404(Article, machine_name=article_machine_name)
    latest_articles = sidebar()

    return render(request, 'blog/index.html', {'article': article, 'latest_articles': latest_articles})

def sidebar():
    latest_articles = Article.objects.order_by('-pub_date')[:10]

    return latest_articles


# @TODO move over into actual api module
class ListArticleView(generics.ListAPIView):
    """
    Provides a get method handler to fetch an article.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer