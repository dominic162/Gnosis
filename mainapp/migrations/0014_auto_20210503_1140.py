# Generated by Django 3.1.6 on 2021-05-03 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_auto_20210502_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extra_info',
            name='bio',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
