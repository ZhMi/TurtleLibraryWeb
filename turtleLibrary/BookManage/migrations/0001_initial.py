# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book_num', models.CharField(max_length=50, verbose_name=b'\xe7\xbc\x96\xe5\x8f\xb7')),
                ('title', models.CharField(max_length=60, verbose_name=b'\xe4\xb9\xa6\xe5\x90\x8d')),
                ('author', models.CharField(max_length=60, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85')),
                ('publish_house', models.CharField(max_length=20, verbose_name=b'\xe5\x87\xba\xe7\x89\x88\xe7\xa4\xbe')),
                ('summary', models.TextField(default=b'', verbose_name=b'\xe6\xa6\x82\xe8\xbf\xb0')),
                ('total_amount', models.IntegerField(null=True, verbose_name=b'\xe6\x80\xbb\xe6\x95\xb0', blank=True)),
                ('lent_amount', models.IntegerField(null=True, verbose_name=b'\xe5\xb7\xb2\xe5\x80\x9f\xe6\x95\xb0\xe9\x87\x8f', blank=True)),
                ('surplus_amount', models.IntegerField(null=True, verbose_name=b'\xe5\x89\xa9\xe4\xbd\x99\xe6\x95\xb0\xe9\x87\x8f', blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x85\xa5\xe5\xba\x93\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4', null=True)),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': '\u4e66\u7c4d',
                'verbose_name_plural': '\u4e66\u7c4d',
            },
        ),
        migrations.CreateModel(
            name='Borrow_records',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('book_num', models.CharField(max_length=50, verbose_name=b'\xe7\xbc\x96\xe5\x8f\xb7')),
                ('borrow_start_time', models.DateTimeField(verbose_name=b'\xe5\x80\x9f\xe5\x87\xba\xe6\x97\xa5\xe6\x9c\x9f')),
                ('limit_day', models.IntegerField(null=True, verbose_name=b'\xe9\x99\x90\xe5\x80\x9f\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('deadline_time', models.DateTimeField(verbose_name=b'\xe5\xbd\x92\xe8\xbf\x98\xe6\x97\xa5\xe6\x9c\x9f')),
                ('overdueday', models.IntegerField(null=True, verbose_name=b'\xe8\xb6\x85\xe6\x9c\x9f\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('fine', models.IntegerField(null=True, verbose_name=b'\xe7\xbd\x9a\xe6\xac\xbe', blank=True)),
                ('renew_times', models.IntegerField(null=True, verbose_name=b'\xe7\xbb\xad\xe5\x80\x9f\xe6\xac\xa1\xe6\x95\xb0', blank=True)),
            ],
            options={
                'ordering': ['borrow_start_time'],
                'verbose_name': '\u7528\u6237\u540d',
                'verbose_name_plural': '\u7528\u6237\u540d',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=60, verbose_name=b'\xe7\xb1\xbb\xe7\x9b\xae')),
                ('intro', models.TextField(default=b'', verbose_name=b'\xe7\xb1\xbb\xe7\x9b\xae\xe7\xae\x80\xe4\xbb\x8b')),
            ],
            options={
                'ordering': ['category_name'],
                'verbose_name': '\u7c7b\u76ee',
                'verbose_name_plural': '\u7c7b\u76ee',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('password', models.CharField(max_length=50, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('borrow_book', models.ManyToManyField(to='BookManage.Book', verbose_name=b'\xe5\x80\x9f\xe9\x98\x85\xe4\xb9\xa6\xe7\xb1\x8d')),
            ],
            options={
                'ordering': ['username'],
                'verbose_name': '\u7528\u6237\u540d',
                'verbose_name_plural': '\u7528\u6237\u540d',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(to='BookManage.Category', verbose_name=b'\xe5\xbd\x92\xe5\xb1\x9e\xe7\xb1\xbb\xe7\x9b\xae'),
        ),
    ]
