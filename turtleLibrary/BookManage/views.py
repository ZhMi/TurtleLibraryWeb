#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from models import User
from models import Book
from models import Category
from models import BorrowRecords

from django.shortcuts import render_to_response
from datetime import *
from django.contrib import admin
from django.conf.urls import patterns, include, url

class UserForm(forms.Form): 
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码  ',widget=forms.PasswordInput())

def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                return HttpResponse('The name has been used,error.')
            #添加到数据库
            User.objects.create(username= username,password=password)
            return HttpResponse('regist success!!')
    else:
        uf = UserForm()
    return render_to_response('regist.html',{'uf':uf}, context_instance=RequestContext(req))

def login(req):
    try:
        response = HttpResponse()
        response.delete_cookie('username')
    except:
        pass 
    if req.method == 'POST':
        uf = UserForm(req.POST)
        response = req.POST
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                #比较成功，跳转index
                response = HttpResponseRedirect('/BookManage/index/')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                #比较失败，还在login
                return HttpResponseRedirect('/BookManage/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(req))

# login in successfully
def index(req):
    username = req.COOKIES.get('username','')
    return render_to_response('index.html' ,{'username':username})

# login out
def logout(req):
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response

# enter the main web page of TurtleLibrary
def entermainpage(req):
	return render_to_response('mainpage.html')

def search_form(request):
    return render_to_response('search_form.html')
# search a book

def search(request):
    '''
    if request.method == 'get':
    '''
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        # books = Book.objects.filter(title__icontains=q)
        books = Book.objects.filter(title__contains=q)
        return render_to_response('search_results.html',{'books': books, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')
    '''
    else:
        return render_to_response('search_form.html')
    return render_to_response('mainpage.html')
    '''
'''
def bad_search(request):
    # The following line will raise KeyError if 'q' hasn't
    # been submitted!
    message = 'You searched for: %r' % request.GET['q']
    return HttpResponse(message)
'''
def search_results(req):
    return render_to_response('search_results.html')


# borrow a book
def borrow(request):
    '''
    if request.method == 'get':
    '''

    ''' 
        RootCount.objects.filter(key = n.key).update(success = F('success') + 1,value = value_str,support = True) 
    '''
    if 'q' in request.GET and request.GET['q']:
    # if 5>3:
        q = request.GET['q']
        #q = request.getRequest().getParameter('q')
        books = Book.objects.filter(book_num__icontains = q)
        for book in books:
            if book.surplus_amount > 0:
                username = request.COOKIES.get('username','')
                user = User.objects.get(username = username)            
                book = Book.objects.get(book_num = q)
                user.borrow_book.add(book)
                now_time = datetime.now()
                dead_time = now_time +  timedelta(days = 20)
                flag = 0
                borrow_times = 0
                book_records = BorrowRecords.objects.filter(username__icontains = username)
                try:     
                    for record in book_records:
                        overdueday = (now_time - record.deadline_time).days
                        borrow_times = borrow_times + 1
                        if overdueday > 0:
                            record.overdueday = overdueday
                            record.fine = 1 * overdueday
                            record.save()
                            flag = 1
                except:
                    pass
                finally:
                    if flag == 1:
                        return render_to_response('OverdueDateResult.html')
                        # return HttpResponse('您有超期欠费未还图书,不可继续借阅,请缴费还书后再借阅')
                    if borrow_times > 10:
                        return render_to_response('OverdueNumResult.html')
                        # return HttpResponse('已经借阅10本 ，不可继续借阅')

                    book.surplus_amount = book.surplus_amount - 1
                    book.lent_amount = book.lent_amount + 1
                    book.save()
                    # user = User.objects.filter(username__icontains = username)[0]
                    # date = time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime())
                    BorrowRecords.objects.create(username= username,book_num = book.book_num,borrow_start_time = now_time,limit_day = 20,deadline_time = dead_time)
                    return render_to_response('borrow.html',{'books': books, 'query': q})
            else: 
                return HttpResponse('剩余数量是 0 本，借阅失败')
    else:
        return HttpResponse('Please submit a search term.')

def OverdueDateResult(req):
    return render_to_response('OverdueDateResult.html')

def OverdueNumResult(req):
    return render_to_response('OverdueNumResult.html')

# person center
def PersonalCenter(req):
    username = req.COOKIES.get('username','')
    book_records = BorrowRecords.objects.filter(username__icontains = username)
    return render_to_response('PersonalCenter.html',{'book_records' : book_records})

def renew(request):
    if 'q' in request.GET and request.GET['q']:
        # id
        q = request.GET['q']
        # q = request.getRequest().getParameter('q')
        book_borrow_records = BorrowRecords.objects.filter(id__icontains = q)
        now_time = datetime.now()
        
        for book_borrow_record in book_borrow_records:
            overdueday = (now_time - book_borrow_record.deadline_time).days
            if overdueday > 0:
                return HttpResponse('超期欠费,不可续借,请缴费还书后再借阅')
            if book_borrow_record.renew_times > 0:
                return HttpResponse('已经续借过 不可以再续借')
        
        book_borrow_record.deadline_time = book_borrow_record.deadline_time + timedelta(days = 20)
        book_borrow_record.renew_times = 1
        book_borrow_record.save()  
        return render_to_response('RenewBook.html',{'book_borrow_records': book_borrow_records})
    else:
        return HttpResponse('Please submit a search term.')

def RenewBook(req):
    return render_to_response('RenewBook.html')



# define a class used to search book and submit data according to the form

# search one book 
# return the summary of the book

