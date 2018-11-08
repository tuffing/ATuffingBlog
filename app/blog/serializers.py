from rest_framework import serializers
from blog.models import Article

#@TODO move over to proper api app
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("headline", "machine_name", "tags", "body", "pub_date", "teaser", "author", "header_image", "header_image_small")