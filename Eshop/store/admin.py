from .models import Customer,Category,Product,Order,AdminProduct,AdminCategory,AdminCustomer
from django.contrib import admin

# Register your models here.

admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer,AdminCustomer)
admin.site.register(Order)
