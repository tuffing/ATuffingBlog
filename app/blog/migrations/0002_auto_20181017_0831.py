# Generated by Django 2.1.1 on 2018-10-17 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default='root', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='header_image',
            field=models.FileField(null=True, upload_to='banners/%Y/%m/%d/'),
        ),
    ]
