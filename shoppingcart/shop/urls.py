from django.contrib import admin
from django.conf.urls import url
from django.urls import path,re_path
from . import views


app_name = 'shop'

urlpatterns = [
    re_path('^$',views.category_products,name='category_products'),
    url(r'^product/(?P<productid>\d+)/$', views.product_detail, name='product_detail'),
    url(r'^category/(?P<categoryid>\d+)/$', views.category_products, name='product_list_by_category'),
]


