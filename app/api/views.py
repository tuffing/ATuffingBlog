from django.shortcuts import render
from blog.serializers import ArticleSerializer
from blog.models import Article
from rest_framework import generics


# Create your views here.
class ListArticleView(generics.ListAPIView):
    """
    Provides a get method handler to fetch an article.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

# Create your views here.
class GetArticleView(generics.RetrieveAPIView):
    """
    Provides a get method handler to fetch an article.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'machine_name'
    lookup_url_kwarg = 'id'

# 
class GetMostRecentArticles(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        start_index = self.request.query_params.get('start_index', 0)
        #count = int(count_query)
        try:
            start_index = int(start_index)
        except:
            start_index = 0

        end_index = self.request.query_params.get('end_index', start_index+1)
        try:
            end_index = int(end_index)
        except:
            end_index = start_index + 1 #default to 1 item

        queryset = Article.objects.order_by('-pub_date')[start_index:end_index]
        

        return queryset