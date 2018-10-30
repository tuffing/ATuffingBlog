from django.shortcuts import get_object_or_404, render 

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .serializers import ArticleSerializer

from .models import Article

site_name = 'A Tuffing Blog'

def index(request):
    latest = Article.objects.order_by('-pub_date')[:1].get()
    context = getSidebarVariables()
    context['article'] = latest
    context['title'] = site_name + ' - Homepage'

    return render(request, 'blog/article.html', context)

def article(request, article_machine_name):
    article = get_object_or_404(Article, machine_name=article_machine_name)
    context = getSidebarVariables()
    context['article'] = article
    context['title'] = article.headline + ' - ' + site_name 

    return render(request, 'blog/article.html', context)

def archive(request, tag):
    archive_list = []
    if tag.lower() == 'all':
        archive_list = Article.objects.order_by('-pub_date')[:10].get()
    else:
        archive_list = Article.objects.filter(tags=tag)

    context = getSidebarVariables()
    context['archive_list'] = archive_list
    context['title'] = tag + ' - ' + site_name 
    context['tag'] = tag

    return render(request, 'blog/archive.html', context)

def getSidebarVariables():
    latest_articles = Article.objects.order_by('-pub_date')[:10]
    tags = Article.tags.tag_model.objects.all()

    return {'latest_articles': latest_articles, 'tags': tags}

def handler404(request, exception):
        context = getSidebarVariables()
        context['title'] = '404 page not found - ' + site_name 

        return render(request,'blog/errors/404.html', context,  status=404)

def handler500(request, exception):
        context = getSidebarVariables()
        context['title'] = '500 Something broke - ' + site_name 

        #context= { 'title' : '500 Something broke - ' + site_name }

        return render(request,'blog/errors/500.html', context,  status=500)


# @TODO move over into actual api module
class ListArticleView(generics.ListAPIView):
    """
    Provides a get method handler to fetch an article.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer