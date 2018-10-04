from django.shortcuts import get_object_or_404, render 

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from .models import Article

def index(request):
    latest_articles = Article.objects.order_by('-pub_date')[:5]
    
    context = { 'latest_articles': latest_articles}
    return render(request, 'blog/index.html', context)

def page(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'blog/page.html', {'article': article})