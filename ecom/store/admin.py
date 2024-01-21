from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["product","price","created_at","in_stock"]