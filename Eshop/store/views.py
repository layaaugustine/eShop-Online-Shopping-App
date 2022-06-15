import email
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from numpy import product
from .models import Product,Category,Customer

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
    if request.method=='GET':
        print(request.method)            # view form to customer
        return render(request,'signup.html')
    else:
        print(request.method)             # customer post details
        postData=request.POST
        first_names = postData.get('firstname')
        last_names = postData.get('lastname')
        phones= postData.get('phone')
        emails= postData.get('email')
        passwords= postData.get('password')
        customer = Customer(first_name =first_names,
                            last_name = last_names,
                            phone = phones,
                            email=emails,
                            password = passwords)
        customer.save()
        
        return render(request,'index.html')


