from django.urls import path
from .views import ListArticleView, GetArticleView, GetMostRecentArticles

#from . import views

app_name = 'api'
urlpatterns = [
    path('articles/all/', ListArticleView.as_view(), name="articles-all"),
    path('articles/get/<id>', GetArticleView.as_view(), name="articles-get"),
    path('articles/recent/', GetMostRecentArticles.as_view(), name="articles-recents")
]
