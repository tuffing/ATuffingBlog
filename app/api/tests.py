from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from blog.models import Article
from blog.serializers import ArticleSerializer


# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_article(headline="", url="", tags="", body="", date = "2018-10-01T23:22:09+00:00", teaser="", author=""):
        if headline != "" and url != "" and body != "":
            Article.objects.create(headline=headline, machine_name=url, tags=tags, body=body, pub_date=date, teaser=teaser, author=author, header_image=None, header_image_small=None)

    def setUp(self):
        # add test data
        self.create_article("one", "one_url", "tag1", "<p>woah1</p>", "2018-10-06T23:22:09+00:00", "teaser", "username")
        self.create_article("two", "two_url", "tag2,tag5", "<p>woah2</p>", "2018-10-07T23:22:09+00:00", "teaser", "username")
        self.create_article("three", "three_url", "tag3", "<p>woah3</p>", "2018-10-08T23:22:09+00:00", "teaser", "username")
        self.create_article("four", "four_url", "tag4", "<p>woah4</p>", "2018-10-09T23:22:09+00:00", "teaser", "username")


class GetAllArticlesTest(BaseViewTest):

    def test_get_all_articles(self):
        """
        This test ensures that all articles added in the setUp method
        exist when we make a GET request to the articles/ endpoint
        """
        # hit the API endpoint
        #response = self.client.get(
        #    reverse("articles-all", kwargs={"version": "v1"})
        #)
        response = self.client.get('/api/v1/articles/all/?format=json')

        # fetch the data from db
        expected = Article.objects.all()
        serialized = ArticleSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)