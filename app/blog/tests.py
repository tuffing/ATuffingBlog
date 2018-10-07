from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Article
from .serializers import ArticleSerializer


# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_article(headline="", url="", body="", date = "2018-10-01T23:22:09+00:00"):
        if headline != "" and url != "" and body != "":
            Article.objects.create(headline=headline, machine_name=url, body=body, pub_date=date)

    def setUp(self):
        # add test data
        self.create_article("one", "one_url", "<p>woah1</p>", "2018-10-06T23:22:09+00:00")
        self.create_article("two", "two_url", "<p>woah2</p>", "2018-10-07T23:22:09+00:00")
        self.create_article("three", "three_url", "<p>woah3</p>", "2018-10-08T23:22:09+00:00")
        self.create_article("four", "four_url", "<p>woah4</p>", "2018-10-09T23:22:09+00:00")


class GetAllArticlesTest(BaseViewTest):

    def test_get_all_articles(self):
        """
        This test ensures that all articles added in the setUp method
        exist when we make a GET request to the articles/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("articles-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Article.objects.all()
        serialized = ArticleSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
# Create your tests here.
