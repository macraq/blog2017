# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 16:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_article_author_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='author_id',
            new_name='author',
        ),
    ]
