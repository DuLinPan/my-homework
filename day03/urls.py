
from django.urls import re_path
from . import views

urlpatterns = [

    # re_path(r'^review/$',views.my_dec(views.RegisterView.as_view())),
    re_path(r'^review/$',views.RegisterView.as_view()),


]