# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-03 05:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_fields_startups_and_tags_optional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(help_text='A label for URL config', max_length=63, unique_for_month='pub_date', verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='post',
            name='startups',
            field=models.ManyToManyField(blank=True, related_name='blog_posts', to='organizer.Startup', verbose_name='startups'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='blog_posts', to='organizer.Tag', verbose_name='tags'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=63, verbose_name='title'),
        ),
    ]
