# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse


def index(request):
    print("index")

    return HttpResponse("index")

def shier(request):
    print("shier")
    return HttpResponse("shier is mine")

def fan(request):
    print("返回")

    return HttpResponse("fan fan fan ~")

def shang(request):
    print("重定向")

    url = reverse("z:shier")
    print(url)

    return redirect(url)