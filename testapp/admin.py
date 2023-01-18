from django.contrib import admin
from testapp.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['ProductId','ProductName','CategoryId','CategoryName']

admin.site.register(Product,ProductAdmin)
