from django.contrib import admin
from .models import Category, Product

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Product, ProductAdmin)