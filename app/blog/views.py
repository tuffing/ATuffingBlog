from django.shortcuts import get_object_or_404, render 

# Create your views here.
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import generics

from .models import Article

site_name = 'A Tuffing Blog'

def index(request):
    latest = Article.objects.order_by('-pub_date')[:1].get()
    context = getSidebarVariables()
    context['article'] = latest
    context['class'] = 'homepage'
    context['title'] = '%s - Homepage' % site_name
    context['description'] = 'Author: %s,  published: %s,  tags: %s, teaser: %s'  % (latest.author, latest.pub_date, latest.tags, latest.teaser)

    return render(request, 'blog/article.html', context)


def fetchArticles(request, offset, exclude_article=None):
    try:
        if exclude_article:
            context = {'article': Article.objects.exclude(machine_name=exclude_article).order_by('-pub_date')[offset:offset + 1].get()}
        else: #.exclude(pub_date__gt=datetime.date(2005, 1, 3), headline='Hello')
            context = {'article': Article.objects.order_by('-pub_date')[offset:offset + 1].get()}
    except ObjectDoesNotExist:
        raise Http404

    return render(request, 'blog/article-nochrome.html', context)

def article(request, article_machine_name):
    article = get_object_or_404(Article, machine_name=article_machine_name)
    context = getSidebarVariables()
    context['article'] = article
    context['class'] = 'article %s' % (article.machine_name)
    context['title'] = '%s - %s' % (article.headline, site_name)
    context['description'] = 'Author: %s,  published: %s, tags: %s, teaser: %s'  % (article.author, article.pub_date, article.tags, article.teaser)


    return render(request, 'blog/article.html', context)

def archive(request, tag):
    archive_list = []
    if tag.lower() == 'all':
        archive_list = Article.objects.order_by('-pub_date')[:10]
    else:
        archive_list = Article.objects.filter(tags=tag)
        if len(archive_list) == 0:
            raise Http404("No such tag exists")

    context = getSidebarVariables()
    context['archive_list'] = archive_list
    context['title'] = '%s - %s' % (tag, site_name) 
    context['description'] = 'Archive page, topic: %s'  % (tag)
    context['class'] = 'archive archive-tag'


    context['tag'] = tag

    return render(request, 'blog/archive.html', context)

def getSidebarVariables():
    latest_articles = Article.objects.order_by('-pub_date')[:10]
    tags = Article.tags.tag_model.objects.all()

    return {'latest_articles': latest_articles, 'tags': tags}

def handler404(request, exception=None):
        context = getSidebarVariables()
        context['title'] = '404 page not found - %s' % site_name
        context['description'] = 'Error page'

        return render(request,'blog/errors/404.html', context,  status=404)

def handler500(request, exception=None):
        context = getSidebarVariables()
        context['title'] = '500 Something broke - %s' % site_name 

        #context= { 'title' : '500 Something broke - ' + site_name }

        return render(request,'blog/errors/500.html', context,  status=500)

