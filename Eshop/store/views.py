from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from numpy import product
from .models import Product,Category

# Create your views here.

# def index(request):
#     datasample = loader.get_template('index.html')
#     print(Product.objects.all())
#     prds=Product.objects.all
#     data={'products':prds}
#     response=datasample.render(data,request)
#     return HttpResponse(response)

def index(request):
    prdts = Product.objects.all()
    catgry=Category.objects.all()
    data={'products':prdts,'category':catgry}
    return render(request,'index.html',data)
