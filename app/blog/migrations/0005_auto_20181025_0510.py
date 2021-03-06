# Generated by Django 2.1.1 on 2018-10-25 05:10

from django.db import migrations, models
import tagulous.models.fields
import tagulous.models.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181018_0826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tagulous_Article_tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField()),
                ('count', models.IntegerField(default=0, help_text='Internal counter of how many times this tag is in use')),
                ('protected', models.BooleanField(default=False, help_text='Will not be deleted when the count reaches 0')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
            bases=(tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.AlterUniqueTogether(
            name='tagulous_article_tags',
            unique_together={('slug',)},
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=tagulous.models.fields.TagField(_set_tag_meta=True, help_text='Enter a comma-separated tag string', to='blog.Tagulous_Article_tags'),
        ),
    ]
