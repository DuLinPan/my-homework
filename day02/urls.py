
from django.urls import re_path
from . import views

app_name = 'ZU'

urlpatterns = [

    re_path(r'^json/$',views.get_json,name='gjson'),
    re_path(r'^head/$',views.head,name='head'),
    re_path(r'^res/$',views.res,name='res'),
    re_path(r'^re_demo/$',views.re_demo,name='re_demo'),
    re_path(r'^jsres/$',views.jsonres,name='jsres'),
    re_path(r'^foo1/$',views.foo1,name='foo1'),
    re_path(r'^foo2/$',views.foo2,name='foo2'),
    re_path(r'^foo3/$',views.foo3,name='foo3'),
    re_path(r'^sessionset/$',views.session_set),
    re_path(r'^sessionget/$',views.session_get),
    re_path(r'^classview/$',views.ClsViews.as_view()),


]