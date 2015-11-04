# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='歌手名字', max_length=30)),
                ('sex', models.IntegerField(default=None, verbose_name='性别', choices=[(0, '男'), (1, '女')], null=True, blank=True)),
                ('summary', models.TextField(verbose_name='简介', max_length=300, null=True, blank=True)),
                ('touxiang', models.CharField(default='/static/img/article/default.jpg', max_length=100, verbose_name='头像')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('rank', models.IntegerField(default=100, verbose_name='排序')),
            ],
            options={
                'verbose_name': '歌手',
                'verbose_name_plural': '歌手',
                'ordering': ['rank', '-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='歌名', max_length=30)),
                ('img', models.CharField(max_length=100, null=True, blank=True)),
                ('url', models.TextField(verbose_name='链接')),
                ('is_top', models.BooleanField(default=False, verbose_name='置顶')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(verbose_name='歌手', to='music.Singer')),
            ],
            options={
                'verbose_name': '歌曲',
                'verbose_name_plural': '歌曲',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Zhuanji',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='专辑名', max_length=30)),
                ('img', models.CharField(max_length=100, null=True, blank=True)),
                ('public_time', models.DateField(null=True, blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('rank', models.IntegerField(default=1000, verbose_name='排序')),
                ('author', models.ForeignKey(verbose_name='歌手', to='music.Singer')),
            ],
            options={
                'verbose_name': '专辑',
                'verbose_name_plural': '专辑',
                'ordering': ['rank', '-create_time'],
            },
        ),
        migrations.AddField(
            model_name='song',
            name='zhuanji',
            field=models.ForeignKey(verbose_name='专辑', to='music.Zhuanji'),
        ),
    ]
