# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-17 06:49
from __future__ import unicode_literals
from django.db import migrations, models

TAGS = (
    # ( tag name, tag slug ),
    ("augmented reality", "augmented-reality"),
    ("big data", "big-data"),
    ("education", "education"),
    ("ipython", "ipython"),
    ("javascript", "javascript"),
    ("jupyter", "jupyter"),
    ("node.js", "node-js"),
    ("php", "php"),
    ("python", "python"),
    ("ruby on rails", "ruby-on-rails"),
    ("ruby", "ruby"),
    ("zend", "zend"),
)

def add_tag_data(apps, schema_editor):
    Tag = apps.get_model('organizer', 'Tag')
    for tag_name, tag_slug in TAGS:
        Tag.objects.create(name=tag_name, slug=tag_slug)
def remove_tag_data(apps, schema_editor):
    Tag = apps.get_model('organizer', 'Tag')
    for _, tag_slug in TAGS:
        tag = Tag.objects.get(slug=tag_slug)
        tag.delete()

class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0002_auto_20170401_1248'),
    ]

    operations = [migrations.RunPython
    (add_tag_data,
     remove_tag_data)
     ]