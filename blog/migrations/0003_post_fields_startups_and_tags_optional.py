# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-21 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='startups',
            field=models.ManyToManyField(blank=True, related_name='blog_posts', to='organizer.Startup'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='blog_posts', to='organizer.Tag'),
        ),
    ]