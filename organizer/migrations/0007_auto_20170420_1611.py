# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-20 08:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0006_newslink_unique_together_slug_startup'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='newslink',
            unique_together=set([('slug', 'startup')]),
        ),
    ]
