# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-16 01:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_author_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
    ]
