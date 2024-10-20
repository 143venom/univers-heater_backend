from django.contrib import admin
from .models import *



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'stock_quantity']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['product','company_name', 'order_date']
    list_filter = ['order_date']
    search_fields = ['user__username']