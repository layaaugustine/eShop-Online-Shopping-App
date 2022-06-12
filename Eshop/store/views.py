from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from numpy import product
from .models import Product,Category

# Create your views here.

def index(request):
    prdts = None
    catgry=Category.get_all_categories()
    categoryID=request.GET.get('Category')
    if categoryID:
        prdts=Product.get_all_product_by_categoryid(categoryID)
    else:
        prdts=Product.objects.all()
    data={}
    data['products']=prdts
    data['categories']=catgry
    return render(request,'index.html',data)


def signup(request):
    return render(request,'signup.html')
