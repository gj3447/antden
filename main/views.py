from django.shortcuts import render
from django.http import HttpResponse
from . import models
from . import database
array = {}
#from .models import Resent
# Create your views here.

def array_add(code,price):
    if len(array[code])>10:
        del array[code][-1]
    array[code].append(price)

def array_print(code):
    result = ''
    for e in array[code]:
        result = result+','+str(e)
    return result

def array_url(request,code):
    codetemp = str(code)
    pramiter = codetemp.lstrip("1")
    print(pramiter)
    result = array_print(pramiter)
    return HttpResponse(result)

def index(request,code):
    codetemp = str(code)
    pramiter = codetemp.lstrip("1")
    stock_list = []
    name = "NONE"
    for e in database.stock_list():
        if pramiter == e[1]:
            name = e[0]
        stock_temp = {'name':e[0],'code':e[1],'price':str(array[e[1]][0])}
        stock_list.append(stock_temp)
    graph = ''
    for e in array[pramiter]:
        graph = graph+','+str(e)

    context = {'stocklist':stock_list,'graph':graph,'name':name}
    return render(request, 'main/main.html',context)

