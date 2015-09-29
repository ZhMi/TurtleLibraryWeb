# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('BookManage', '0003_auto_20150926_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=60, verbose_name='\u4f5c\u8005'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_num',
            field=models.CharField(max_length=50, verbose_name='\u7f16\u53f7'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(to='BookManage.Category', verbose_name='\u5f52\u5c5e\u7c7b\u76ee'),
        ),
        migrations.AlterField(
            model_name='book',
            name='lent_amount',
            field=models.IntegerField(null=True, verbose_name='\u5df2\u501f\u6570\u91cf', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u5165\u5e93\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publish_house',
            field=models.CharField(max_length=20, verbose_name='\u51fa\u7248\u793e'),
        ),
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='\u7b80\u4ecb', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='surplus_amount',
            field=models.IntegerField(null=True, verbose_name='\u5269\u4f59\u6570\u91cf', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=60, verbose_name='\u4e66\u540d'),
        ),
        migrations.AlterField(
            model_name='book',
            name='total_amount',
            field=models.IntegerField(null=True, verbose_name='\u603b\u6570', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4', null=True),
        ),
        migrations.AlterField(
            model_name='borrowrecords',
            name='book_num',
            field=models.CharField(max_length=50, verbose_name='\u4e66\u7c4d\u7f16\u53f7'),
        ),
        migrations.AlterField(
            model_name='borrowrecords',
            name='borrow_start_time',
            field=models.DateTimeField(verbose_name='\u501f\u51fa\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='borrowrecords',
            name='deadline_time',
            field=models.DateTimeField(verbose_name='\u5f52\u8fd8\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='borrowrecords',
            name='fine',
            field=models.IntegerField(null=True, verbose_name='\u7f5a\u6b3e', blank=True),
        ),
        migrations.AlterField(
            model_name='borrowrecords',
            name='limit_day',
            field=models.IntegerField(null=True, verbose_name='\u9650\u501f\u5929\u6570', blank=True),
        ),
        migrations.AlterField(
            model_name='borrowrecords',
            name='overdueday',
            field=models.IntegerField(null=True, verbose_name='\u8d85\u671f\u65f6\u95f4', blank=True),
        ),
        migrations.AlterField(
            model_name='borrowrecords',
            name='renew_times',
            field=models.IntegerField(null=True, verbose_name='\u7eed\u501f\u6b21\u6570', blank=True),
        ),
        migrations.AlterField(
            model_name='borrowrecords',
            name='username',
            field=models.CharField(max_length=50, verbose_name='\u7528\u6237\u540d'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=60, verbose_name='\u7c7b\u76ee'),
        ),
        migrations.AlterField(
            model_name='category',
            name='intro',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='\u7c7b\u76ee\u7b80\u4ecb', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='borrow_book',
            field=models.ManyToManyField(to='BookManage.Book', verbose_name='\u501f\u9605\u4e66\u7c4d'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50, verbose_name='\u5bc6\u7801'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, verbose_name='\u7528\u6237\u540d'),
        ),
    ]
