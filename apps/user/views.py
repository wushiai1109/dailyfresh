from django.shortcuts import render


# /user/register
# GET POST PUT DELETE OPTION
def register(request):
    '''注册'''
    # 显示注册页面
    return render(request, 'register.html')

def register_hanle(request):
    '''进行页面注册'''
    