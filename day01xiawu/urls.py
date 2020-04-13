
from django.urls import re_path
from . import views

urlpatterns = [

    re_path(r'^rq/$',views.rq),
    re_path(r'^cheng/([a-z]+)/(\d{4})/$',views.we),
    re_path(r'^poo/',views.poo),

]

