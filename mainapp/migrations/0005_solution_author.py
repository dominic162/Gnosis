# Generated by Django 3.1.6 on 2021-03-07 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20210307_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.appuser'),
        ),
    ]
