# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-17 04:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_author'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='post',
            index_together=set([('slug', 'pub_date')]),
        ),
    ]
