from atexit import register
from distutils.sysconfig import customize_compiler
import email
from itertools import product
from tkinter.tix import Tree
from django.db import models
from django.contrib import admin
from django.http import HttpRequest
import datetime

# Create your models her

# ----------------CATEGORY------------------

class Category(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

# -----------------PRODUCT---------------------

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=200,default='',null=True,blank=True)
    image = models.ImageField(upload_to='upload/models/')


    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)       #ids is a list

    @staticmethod
    def get_all_product():
        return Product.objects.all()

    @staticmethod
    def get_all_product_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_product()


# foreign key for link two table

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

# -----------------CUSTOMER------------------------

class Customer(models.Model):
    first_name =models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    phone =models.CharField(max_length=10)
    email=models.EmailField()
    password =models.CharField(max_length=10)

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False
    
    
class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name']



# -----------------ORDER------------------------

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50,default='',blank=True)
    phone = models.CharField(max_length=50,default='',blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

 
    def placeOrder(self):
        self.save()


    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer = customer_id).order_by('-date')



  
