from django.contrib import admin
from django.conf.urls import url
from django.urls import path,re_path
from . import views


app_name = 'shop'

urlpatterns = [
    path('admin/',admin.site.urls),
]