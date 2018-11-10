from django.urls import reverse
from django.shortcuts import get_object_or_404, render 
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

    def test_api_get_all_articles(self):
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

    def test_api_get_article(self):
        """
        Test fetching an article by machine_name
        """
        response = self.client.get('/api/v1/articles/get/two_url?format=json')

        # fetch the data from db
        expected = Article.objects.get(machine_name='two_url')
        serialized = ArticleSerializer(expected, many=False)
        test = serialized.data
        self.assertEqual(response.data, test)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_most_recent_article(self):
        """
        Test fetching most recent article 
        """
        response = self.client.get('/api/v1/articles/recent/?format=json')

        # fetch the data from db
        expected = Article.objects.filter(machine_name='four_url')
        serialized = ArticleSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_most_recent_article_offset_single(self):
        """
        Test fetching most recent article with an offset
        """
        response = self.client.get('/api/v1/articles/recent/?start_index=1&format=json')

        # fetch the data from db
        expected = Article.objects.filter(machine_name='three_url')
        serialized = ArticleSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_most_recent_article_range(self):
        """
        Test fetching most recent article using a range
        """
        response = self.client.get('/api/v1/articles/recent/?start_index=1&end_index=3&format=json')

        # fetch the data from db
        expected = Article.objects.order_by('-pub_date')[1:3]
        serialized = ArticleSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)