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
        # prdts=Product.objects.all()
        prdts=Product.get_all_product()
    data={'products':prdts,'categories':catgry}
    # data['products']=prdts
    # data['categories']=catgry
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
        
        #validation

        value = {
            'firstz_name':first_names,
            'lastz_name' :last_names,
            'phonez' : phones,
            'emailz' :emails
        }

        error_message = None

        if (not first_names):
            error_message="First Name Required !!!"
        elif len(first_names)<4:
            error_message = "First Name must be 4 char long  or more "
        elif (not last_names):
            error_message="Last Name Required !!!"
        elif len(last_names)<4:
             error_message = "Last Name must be 4 char long  or more "
        elif (not phones):
            error_message="Phone Number Required !!!"
        elif len(phones)!=10:
            error_message="Phone Number Must be 10"
        elif (not passwords):
            error_message="Password Required !!!"
        elif len(passwords)<6:
            error_message="Password Must be 6 char long"
        elif len(emails)<5:
            error_message="Email must be 5 char long"

        # saving
        if not error_message:
            customer = Customer(first_name =first_names,
                                last_name = last_names,
                                phone = phones,
                                email=emails,
                                password = passwords)
            customer.save()
            return render(request,'index.html')
        else:
            data={
                'error':error_message,                            # if we have error,entered data automatic save,its add in signup page too
                'values':value
            }
            return render(request,'signup.html',data)

### 25
