from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from store.models import Product


# Create your views here.
#takes a request and response 
#request handler 


def say_hello(request): 
    try:
        product = Product.objects.get(pk=1)
    except ObjectDoesNotExist:
        pass
    
    

    return render(request,'hello.html',{'name' : 'Santoshgpt'})
