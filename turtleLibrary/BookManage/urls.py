from django.conf.urls import patterns, url

from BookManage import views
from django.contrib import admin
from django.conf.urls import include 

admin.autodiscover() 

urlpatterns = patterns('',
    # url(r'^admin/$', include(admin.site.urls)),
    url(r'^$', views.login, name='login'),
    url(r'^login/$',views.login,name = 'login'),
    url(r'^regist/$',views.regist,name = 'regist'),
    url(r'^index/$',views.index,name = 'index'),
    url(r'^logout/$',views.logout,name = 'logout'),
    
    # add entermainpage url
    url(r'^entermainpage/$',views.entermainpage,name = 'entermainpage'),
    url(r'^search/$',views.search,name = 'search'),
    url(r'^borrow/$',views.borrow,name = 'borrow'),
    url(r'^PersonalCenter/$',views.PersonalCenter,name = 'PersonalCenter'),
    url(r'^search_results/$',views.search_results,name = 'search_results'),
    url(r'^search_form/$',views.search_form,name = 'search_form'),
    # url(r'^bad_search/$',views.bad_search,name = 'bad_search'),
    url(r'^borrow/$',views.borrow,name = 'borrow'),
    # OverdueDateResult
    url(r'^OverdueDateResult/$',views.OverdueDateResult,name = 'OverdueDateResult'),
    # OverdueNumResult
    url(r'^OverdueNumResult/$',views.OverdueNumResult,name = 'OverdueNumResult'), 
    # book_borrow_record
    url(r'^RenewBook/$',views.RenewBook,name = 'RenewBook'), 
              
)