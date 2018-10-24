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
    
    context = { 'latest': latest, 'latest_articles': latest_articles}
    return render(request, 'blog/index.html', context)

def page(request, article_machine_name):
    article = get_object_or_404(Article, machine_name=article_machine_name)
    return render(request, 'blog/article.html', {'article': article})

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