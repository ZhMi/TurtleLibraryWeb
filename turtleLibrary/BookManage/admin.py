# coding=utf8

from __future__ import unicode_literals
from django.contrib import admin
from django.db import models
from .models import Book,User,Category,BorrowRecords

# from django.conf.urls import patterns

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('category_name','intro')
	search_fields = ('category_name','intro')
	def get_search_results(self, request, queryset, search_term):
		queryset, use_distinct = super(CategoryAdmin, self).get_search_results(request, queryset, search_term)
		try:
			# search_term_as_int = int(search_term)
			search_term_as_int = search_term
			
			queryset |= self.model.objects.filter(category_name = search_term_as_int)
		except:
			pass
		return queryset, use_distinct

class BookAdmin(admin.ModelAdmin):
	list_display = ('book_num','title','author','pub_date','update_time')
	# codes
	search_fields = ('book_num','title','author','pub_date','update_time')
	def get_search_results(self, request, queryset, search_term):
		queryset, use_distinct = super(BookAdmin, self).get_search_results(request, queryset, search_term)
		try:
			# search_term_as_int = int(search_term)
			search_term_as_int = search_term
			
			queryset |= self.model.objects.filter(book_num = search_term_as_int)
		except:
			pass
		return queryset, use_distinct

class UserAdmin(admin.ModelAdmin):
	list_display = ('username','password')
	search_fields = ('username','password')
	def get_search_results(self, request, queryset, search_term):
		queryset, use_distinct = super(UserAdmin, self).get_search_results(request, queryset, search_term)
		try:
			# search_term_as_int = int(search_term)
			search_term_as_int = search_term
			
			queryset |= self.model.objects.filter(username = search_term_as_int)
		except:
			pass
		return queryset, use_distinct

class BorrowRecordsAdmin(admin.ModelAdmin):
	list_display = ('username','book_num','borrow_start_time','deadline_time','overdueday','fine','renew_times')
	search_fields = ('username','book_num','borrow_start_time','deadline_time','overdueday','fine','renew_times')
	def get_search_results(self, request, queryset, search_term):
		queryset, use_distinct = super(BorrowRecordsAdmin, self).get_search_results(request, queryset, search_term)
		try:
			# search_term_as_int = int(search_term)
			search_term_as_int = search_term
			
			queryset |= self.model.objects.filter(book_num = search_term_as_int)
		except:
			pass
		return queryset, use_distinct

class MyModelAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(MyModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(author=request.user)

admin.site.register(Book,BookAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(BorrowRecords,BorrowRecordsAdmin)

