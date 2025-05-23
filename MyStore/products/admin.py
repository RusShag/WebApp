from django.contrib import admin
from .models import Category, Product, Cart, CartItem

admin.site.register(Cart)
admin.site.register(CartItem)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category', )
    search_fields = ('name', 'description')
