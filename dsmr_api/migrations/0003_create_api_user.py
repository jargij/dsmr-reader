# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 19:56
from __future__ import unicode_literals

from django.db import migrations
from django.conf import settings


def migrate_forward(apps, schema_editor):
    User = apps.get_model('auth', 'User')

    if User.objects.filter(username=settings.DSMRREADER_REST_FRAMEWORK_API_USER).exists():
        return

    User.objects.create(
        username=settings.DSMRREADER_REST_FRAMEWORK_API_USER,
        email='root@localhost'
    )


def migrate_backward(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.filter(username=settings.DSMRREADER_REST_FRAMEWORK_API_USER).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('dsmr_api', '0002_generate_random_auth_key'),
    ]

    operations = [
        migrations.RunPython(migrate_forward, migrate_backward),
    ]