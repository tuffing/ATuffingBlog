# Generated by Django 2.1.1 on 2018-10-28 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_article_teaser'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='header_image_small',
            field=models.FileField(null=True, upload_to='banners/%Y/%m/%d/'),
        ),
    ]
