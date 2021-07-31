from django.contrib import admin

from .models import Category, Product, Content, Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_status', 'time_create', 'user_phone',)
    search_fields = ('user_name', 'user_status', 'user_phone', 'user_email')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    search_fields = ('name', 'status', 'category')



admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Content)
admin.site.register(Order, OrderAdmin)