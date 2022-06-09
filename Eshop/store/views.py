from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from numpy import product
from .models import Product

# Create your views here.

def index(request):
    datasample = loader.get_template('Order/order.html')
    print(Product.objects.all())
    prds=Product.objects.all
    data={'products':prds}
    response=datasample.render(data,request)
    return HttpResponse(response)