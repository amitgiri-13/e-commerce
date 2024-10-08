from django.contrib import admin
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["product","price","created_at","in_stock"]
   

class CartItemsInline(admin.TabularInline):
    model = CartItems
    extra = 1 

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemsInline]
    
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(Review)