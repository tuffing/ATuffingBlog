from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from tagulous.models import TagField

class Article(models.Model):
    
    headline = models.CharField(max_length=200)
    machine_name =  models.CharField(max_length=40)
    author = models.CharField(max_length=50)
    teaser = RichTextUploadingField(null = True)
    body = RichTextUploadingField()
    pub_date = models.DateTimeField('date published')
    header_image  = models.FileField(upload_to='banners/%Y/%m/%d/', null=True)
    tags = TagField()


    def __str__(self):
        return self.headline


class AltHeadlines(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    headline = models.CharField(max_length=200)
    used = models.IntegerField(default=0)

    def __str__(self):
        return self.headline
