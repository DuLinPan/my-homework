from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View


def my_dec(func):
    def inner(request,*args,**kwargs):
        print("自定义的装饰器被调用了")
        print("请求路径：%s"%request.path)

        return func(request,*args,**kwargs)
    return inner

def my_dec2(func):
    def inner(request,*args,**kwargs):
        print("自定义的装饰器2被调用了")
        print("请求路径2：%s"%request.path)

        return func(request,*args,**kwargs)
    return inner

class OneMiXin(object):
    @classmethod
    def as_view(cls,*args,**kwargs):
        view = super().as_view(*args,**kwargs)
        view = my_dec(view)
        return view


class TwoMiXin(object):
    @classmethod
    def as_view(cls,*args,**kwargs):
        view = super().as_view(*args,**kwargs)
        view = my_dec2(view)
        return view

# @method_decorator(my_dec,name='get')
# @method_decorator(my_dec,name='post')
# @method_decorator(my_dec,name='dispatch')
class RegisterView(OneMiXin,TwoMiXin,View):
    def get(self,request):
        print("Register get")

        return HttpResponse("Register get")

    def post(self, request):
        print("Register post")

        return HttpResponse("Register post")



