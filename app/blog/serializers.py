from rest_framework import serializers
from .models import Article

#@TODO move over to proper api app
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("headline", "machine_name", "body", "pub_date")