# from django.shortcuts import render

# Create your views here.

# 查询字符串参数
from django.http import HttpResponse


def rq(request):

    a = request.GET.get('a')
    b = request.GET.get('b')
    alist = request.GET.getlist('a')

    print(a)
    print(b)
    print(alist)

    return HttpResponse("go home")

def we(request,city,date):

    print("city",city)
    print("date",date)


    return HttpResponse("we")


def poo(request):

    a = request.POST.get("a")
    b = request.POST.get("b")
    alist = request.POST.getlist("a")

    print(a)
    print(b)
    print(alist)

    return HttpResponse("poo poo poo")