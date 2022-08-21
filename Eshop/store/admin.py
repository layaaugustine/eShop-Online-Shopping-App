
from django.contrib import admin
from .models import Category, Customer, Product,AdminProduct,AdminCategory,Customer,AdminCustomer,Order
# Register your models here.

admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer,AdminCustomer)
admin.site.register(Order)


