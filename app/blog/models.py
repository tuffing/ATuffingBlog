from django.db import models


class Article(models.Model):
    headline = models.CharField(max_length=200)
    machine_name =  models.CharField(max_length=40)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.headline


class AltHeadlines(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    headline = models.CharField(max_length=200)
    used = models.IntegerField(default=0)

    def __str__(self):
        return self.headline
