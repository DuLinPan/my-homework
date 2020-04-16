def my_middleware(get_response):

    print("工程初始化执行的代码")

    def middleware(request):

        print('get_response执行之前的代码')

        response = get_response(request)

        print('get_response执行之后的代码')

        return response

    return middleware

