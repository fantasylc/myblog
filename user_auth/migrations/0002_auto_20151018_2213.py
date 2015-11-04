# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='img',
        ),
        migrations.AlterField(
            model_name='user',
            name='intro',
            field=models.TextField(null=True, blank=True, verbose_name='简介'),
        ),
    ]
