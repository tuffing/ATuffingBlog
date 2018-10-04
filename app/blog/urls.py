from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /blog/5/
    path('<int:article_id>/', views.page, name='page'),
]