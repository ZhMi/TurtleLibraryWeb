# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField
from django.contrib import admin
from django.conf.urls import patterns



class Category(models.Model):
	category_name = models.CharField('类目',max_length = 60)
	# intro = models.TextField('类目简介', default = '')
	intro = UEditorField('类目简介', height=300, width=1000,default=u'', blank=True, imagePath="uploads/images/",toolbars='besttome', filePath='uploads/files/')
	def __unicode__(self):
		return self.category_name
	class Meta:
		verbose_name = '类目'
		verbose_name_plural = '类目'
		ordering = ['category_name']


class Book(models.Model):
	book_num = models.CharField('编号',max_length = 50)
	title = models.CharField('书名',max_length = 60)
	author = models.CharField('作者',max_length = 60)
	publish_house = models.CharField('出版社',max_length = 20)
	category = models.ManyToManyField(Category, verbose_name='归属类目')
	# summary = models.TextField('概述',default = '')
	summary = UEditorField('简介', height=300, width=1000,default=u'', blank=True, imagePath="uploads/images/",toolbars='besttome', filePath='uploads/files/')
	total_amount = models.IntegerField('总数',blank=True, null=True)
	lent_amount = models.IntegerField('已借数量',blank=True, null=True)
	surplus_amount = models.IntegerField('剩余数量',blank=True, null=True)
	pub_date = models.DateTimeField('入库时间', auto_now_add=True, editable=True)
	update_time = models.DateTimeField('更新时间', auto_now=True, null=True)
	def __unicode__(self):
		return self.title
	class Meta:
		verbose_name = '书籍'
		verbose_name_plural = '书籍'
		ordering = ['title']


class User(models.Model):
	username = models.CharField('用户名',max_length = 50)
	password = models.CharField('密码',max_length = 50)
	borrow_book = models.ManyToManyField(Book, verbose_name='借阅书籍')
	def __unicode__(self):
		return self.username
	class Meta:
		verbose_name = '读者'
		verbose_name_plural = '读者'
		ordering = ['username']


class BorrowRecords(models.Model):
	username = models.CharField('用户名',max_length = 50)
	book_num = models.CharField('书籍编号',max_length = 50)
	borrow_start_time = models.DateTimeField('借出日期',auto_now = False)
	limit_day = models.IntegerField('限借天数',blank=True, null=True)	
	deadline_time = models.DateTimeField('归还日期',auto_now = False)	
	overdueday = models.IntegerField('超期时间',blank=True, null=True)
	fine = models.IntegerField('罚款',blank=True, null=True)
	renew_times = models.IntegerField('续借次数',blank=True, null=True)
	def __unicode__(self):
		return self.username
	class Meta:
		verbose_name = '借阅记录'
		verbose_name_plural = '借阅记录'
		ordering = ['borrow_start_time']

