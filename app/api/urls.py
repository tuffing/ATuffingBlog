from django.urls import path
from .views import ListArticleView

#from . import views

app_name = 'api'
urlpatterns = [
    path('articles/all/', ListArticleView.as_view(), name="articles-all")
]
