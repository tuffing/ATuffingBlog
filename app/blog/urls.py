from django.urls import path
from .views import index, page,ListArticleView

#from . import views

app_name = 'blog'
urlpatterns = [
    path('', index, name='index'),
    # ex: /blog/5/
    path('<int:article_id>/', page, name='page'),
    #path('blog/', ListArticleView.as_view(), name="articles-all")
]

