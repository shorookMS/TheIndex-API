# Generated by Django 2.0.2 on 2018-02-17 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_author_imageurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='imageUrl',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]