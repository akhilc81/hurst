from django.contrib import admin

from . models import Product,Contact

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=("product_name","product_price")
    
admin.site.register(Contact)    

# @admin.register(Contact)
# class ContactAdmin(admin.ModelAdmin):
#     list_display=("customer_name","customer_email","customer_message")


