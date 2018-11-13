from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Article


# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_article(headline="", url="", tags="", body="", date = "2018-10-01T23:22:09+00:00", teaser="", author=""):
        if headline != "" and url != "" and body != "":
            Article.objects.create(headline=headline, machine_name=url, tags=tags, body=body, pub_date=date, teaser=teaser, author=author, header_image="banners/2018/10/24/935x200.png", header_image_small="banners_small/2018/10/28/250x80.png")

    def setUp(self):
        # add test data
        self.create_article("one", "one_url", "tag1", "<p>woah1</p>", "2018-10-06T23:22:09+00:00", "teaser", "username")
        self.create_article("two", "two_url", "tag2,tag5", "<p>woah2</p>", "2018-10-07T23:22:09+00:00", "teaser", "username")
        self.create_article("three", "three_url", "tag3", "<p>woah3</p>", "2018-10-08T23:22:09+00:00", "teaser", "username")
        self.create_article("four", "four_url", "tag4", "<p>woah4</p>", "2018-10-09T23:22:09+00:00", "teaser", "username")



class BlogTests(BaseViewTest):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_article_page_good(self):
        response = self.client.get('/two_url/')
        self.assertEqual(response.status_code, 200)

    def test_article_page_bad(self):
        response = self.client.get('/fake_url/')
        self.assertEqual(response.status_code, 404)

    def test_archive_page_all_good(self):
        response = self.client.get('/archive/all/')
        self.assertEqual(response.status_code, 200)

    def test_archive_page_tag_good(self):
        response = self.client.get('/archive/tag1/')
        self.assertEqual(response.status_code, 200)

    def test_archive_page_tag_multi_good(self):
        response = self.client.get('/archive/tag5/')
        self.assertEqual(response.status_code, 200)

    def test_archive_page_tag_bad(self):
        response = self.client.get('/archive/fake_tag/')
        self.assertEqual(response.status_code, 404)

    def test_fetch_articles_offset_good(self):
        response = self.client.get('/fetchArticlesOffset/1/')
        self.assertEqual(response.status_code, 200)

    def test_fetch_articles_offset_out_of_range(self):
        response = self.client.get('/fetchArticlesOffset/4/')
        self.assertEqual(response.status_code, 404)

    def test_fetch_articles_offset_not_int(self):
        response = self.client.get('/fetchArticlesOffset/notanint/')
        self.assertEqual(response.status_code, 404)