# Generated by Django 3.1.6 on 2021-03-31 18:25

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('mainapp', '0009_auto_20210313_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]