from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_world(request):
    """简单的学号姓名视图函数"""
    return HttpResponse("<h1>20221201016 邬永眺</h1><p>")

def hello_name(request, name):
    """带参数的学号姓名视图函数"""
    return HttpResponse(f"<h1>20221201016 邬永眺 {name}!</h1><p>")
