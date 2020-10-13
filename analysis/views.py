from django.shortcuts import render

from django.shortcuts import HttpResponse #导入HttpResponse模块

# Create your views here.
def analysis(request): #request是必须带的实例。类似class下方法必须带self一样, 
    message = '感谢确认，请使用账户登录！'
    return render(request, 'analysis.html', {'message': message})
    #return HttpResponse("Hello World")#通过HttpResponse模块直接返回字符串到前端页面