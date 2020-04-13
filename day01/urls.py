from django.urls import re_path
from . import views

app_name = 'z'

urlpatterns = [

    re_path(r'^index/$',views.index,name='index'),
    re_path(r'^shier/$',views.shier,name='shier'),
    re_path(r'^fan/$',views.fan,name='fan'),
    re_path(r'^shang/$',views.shang,name='shang'),
]