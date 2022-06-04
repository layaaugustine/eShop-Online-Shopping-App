
from django.contrib import admin
from .models import Category, Product,AdminProduct,AdminCategory
# Register your models here.

admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
