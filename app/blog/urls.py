from django.urls import path
from .views import ListArticleView

#from . import views

app_name = 'blog'
urlpatterns = [
    #path('', views.index, name='index'),
    # ex: /blog/5/
    #path('<int:article_id>/', views.page, name='page'),
    path('blog/', ListArticleView.as_view(), name="articles-all")
]

