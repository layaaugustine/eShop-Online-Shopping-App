from .models import Customer,Category,Product,Order,AdminProduct,AdminCategory
from django.contrib import admin

# Register your models here.

admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Order)
