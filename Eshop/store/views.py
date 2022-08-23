import email
from operator import add
from pydoc import classname
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from matplotlib.pyplot import cla
from numpy import product
from .models import Product,Category,Customer,Order

from django.contrib.auth.hashers import make_password,check_password

from django.views import View
# from .middlewares.auth import auth_middleware
# from django.utils.decorators import method_decorator

# Create your views here.


# print(make_password('1234'))
# print(check_password('1234','pbkdf2_sha256$320000$PkZpFTYwnHJqneea3kucX6$8I9DcV9CKqGsLywdUVnphUwdtGgQm61MOuIjmQSm9CE='))



def front(request):
    return render(request,'front.html')

# index in class

class Index(View):

    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart']={}
         # prdts = None
        catgry=Category.get_all_categories()
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
        print('you are :',request.session.get('email'))
        return render(request,'index.html',data)

    def post(self,request):
        product=request.POST.get('product_id')
        remove= request.POST.get('remove')
        cart=request.session.get('cart')
        print("my old cart",cart)

    
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart']=cart
        print("my current cart",request.session['cart'])
        return redirect('homepage')

# index



class Signup(View):
    def get(self,request):
        return render(request,'signup.html')
    def post(self,request):
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
        




class Login(View):

    # return_url = None     # url (last)

    def get(self,request):

        # Login.return_url = request.GET.get('return_url')
        return render(request,'login.html')

    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.get_customer_by_email(email)

        error_message = None
        
        if customer:
            flag=check_password(password , customer.password)

            if flag:

                request.session['customer']=customer.id
                

                # if Login.return_url:
                #     return HttpResponseRedirect(Login.return_url)
                # else:
                #     Login.return_url =  None
                return redirect('homepage')

            else:
                error_message = "invalid password"
        else:
            error_message="invalid  email "

        print(email,password)
        
        return render(request,'login.html',{'error':error_message})
        


def logout(request):
    request.session.clear()
    return redirect('login')



class Cart(View):
    def get(self,request):
        # print(list(request.session.get('cart').keys()))
        ids=list(request.session.get('cart').keys())
        products=Product.get_products_by_id(ids)
        print(products)
        return render(request,'cart.html',{
            'products':products
        })

class Checkout(View):
    def post(self, request):
        # print(request.POST)
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart=request.session.get('cart')

        products = Product.get_products_by_id(list(cart.keys()))

        print("id of product : number of product :",cart)
        print("product :",products)
        print("cuustomer id :",customer)
        print(address)
        print(phone)


        for product in products:
            order = Order( customer=Customer(id=customer),
                product=product,
                price = product.price,
                address = address,
                phone = phone,
                quantity=cart.get(str(product.id))
                )

            order.save()
        request.session['cart'] = {}

        return redirect('cart')


class OrderView(View):

   
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request,'orders.html',{
            'orders':orders
        })

    