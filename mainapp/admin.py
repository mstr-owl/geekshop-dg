from django.contrib import admin

from mainapp.models import ProductCategories, Product

admin.site.register(ProductCategories)
admin.site.register(Product)
