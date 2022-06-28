import email
from django.db import models
from django.contrib import admin
from django.http import HttpRequest
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


    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False

class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name']
    
    

  
