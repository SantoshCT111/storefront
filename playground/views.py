from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#takes a request and response 
#request handler 
def calculate():
    x=1
    y =2 
    return x+y

def say_hello(request): 
    x=calculate()
    return render(request,'hello.html',{'name' : 'Santoshgpt'})
