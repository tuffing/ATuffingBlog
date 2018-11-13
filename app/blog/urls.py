from django.urls import path
from .views import index, article,archive,fetchArticles

#from . import views

app_name = 'blog'
urlpatterns = [
    path('', index, name='index'),
    path('fetchArticlesOffset/<int:offset>/', fetchArticles, name='fetchArticles'),
    # ex: /blog/5/
    path('<article_machine_name>/', article, name='article'),
    path('archive/<tag>/', archive, name='archive'),
    #path('blog/', ListArticleView.as_view(), name="articles-all")
]
