import email
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from numpy import product
from .models import Product,Category,Customer

from django.contrib.auth.hashers import make_password,check_password

from django.views import View

# Create your views here.


# print(make_password('1234'))
# print(check_password('1234','pbkdf2_sha256$320000$PkZpFTYwnHJqneea3kucX6$8I9DcV9CKqGsLywdUVnphUwdtGgQm61MOuIjmQSm9CE='))

# index

def index(request):
    # prdts = None
    catgry=Category. get_all_categories()
    # catgry=Category.objects.all()              
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
      
#signup

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
        # return registerUser(request)


        #validation

        value = {
            'firstz_name':first_names,
            'lastz_name' :last_names,
            'phonez' : phones,
            'emailz' :emails
        }

        error_message = None

        customer = Customer(first_name =first_names,
                                last_name = last_names,
                                phone = phones,
                                email=emails,
                                password=passwords)

        # validateCustomer(customer)

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

        elif customer.isExists():
            error_message="Email address already Exist!!"
      

        # saving 



        if not error_message:
            # customer = Customer(first_name =first_names,
            #                     last_name = last_names,
            #                     phone = phones,
            #                     email=emails,
            #                     password = passwords)
            customer.password=make_password(customer.password)    # Encoding form
            customer.save()
            return redirect('homepage')
        else:
            data={
                'error':error_message,                            # if we have error,entered data automatic save,its add in signup page too
                'values':value
            }
            return render(request,'signup.html',data)
            


# login   inside class

class Login(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.get_customer_by_email(email)

        error_message = None
        
        if customer:
            flag=check_password(password , customer.password)
            if flag:
                return redirect('homepage')
            else:
                error_message = "invalid password"
        else:
            error_message="invalid  email "

        print(email,password)
        
        return render(request,'login.html',{'error':error_message})
        



# login without use class method

# def login(request):
    # if request.method =='GET':
    #     print(request.method)
    #     return render(request,'login.html')
    # else:
    #     email=request.POST.get('email')
    #     password=request.POST.get('password')
    #     customer=Customer.get_customer_by_email(email)

    #     error_message = None
        
    #     if customer:
    #         flag=check_password(password , customer.password)
    #         if flag:
    #             return redirect('homepage')
    #         else:
    #             error_message = "invalid password"
    #     else:
    #         error_message="invalid  email "

    #     print(email,password)
        
    #     return render(request,'login.html',{'error':error_message})
        

    
        