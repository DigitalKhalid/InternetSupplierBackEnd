from django.contrib import admin
from .models import ProductType, ProductCatagory, Product

admin.site.register(ProductType)
admin.site.register(ProductCatagory)
admin.site.register(Product)
