from django.http import HttpResponse, JsonResponse
import json

# JSON形式传参（前端传递参数的最后一种方式）
from django.shortcuts import redirect
from django.urls import reverse


def get_json(request):

    # 获取 json 类型数据:
    json_bytes = request.body
    # 将 bytes 类型转为 str
    json_str = json_bytes.decode()
    # 将 str 转为 dict
    dict = json.loads(json_str)

    print(dict.get('a'))
    print(dict.get('b'))

    return HttpResponse('get_json')


# 请求头函数
def head(request):
    print(request.META['CONTENT_TYPE'])
    print(request.META['CONTENT_LENGTH'])

    return HttpResponse("head")

# 响应函数
def res(request):

    str = '{"name":"python"}'

    print(str)

    return HttpResponse(str,
                        content_type='application/json',
                        status=200)


def re_demo(request):
    # 创建一个 response 对象
    response = HttpResponse('itcast python', status=400)

    # 在 response 对象中添加一个新的键值对
    response['Itcast'] = 'Python'

    # 返回 response
    return response


# JsonResopnse类 ：可以自动把字典转成JSON字符串
def jsonres(request):

    dict = {'city':'xian',
            'weather':'sunny'}

    print(dict)

    return JsonResponse(dict)

# redirect 重定向
def foo1(request):

    print("foo1函数打印")

    return HttpResponse("foo1")

def foo2(request):

    print("foo2函数打印")

    return HttpResponse("foo2")

def foo3(request):

    print("foo3函数打印")

    url = reverse("ZU:foo1")

    print(url)

    return redirect(url)


# ssesion 操作

# 写入数据
def session_set(request):

    request.session['myname']='dulinpan'

    return HttpResponse("session_demo")

# 获取数据
def session_get(request):

    value = request.session.get('myname')

    print(value)

    return HttpResponse(value)

from django.http import HttpResponse
from django.views.generic import View


class ClsViews(View):

    def get(self,request):
        print("类视图 GET方法")
        return HttpResponse("类视图 GET方法")

    def post(self,request):
        print("类视图 post方法")
        return HttpResponse("类视图 post方法")
