from django.contrib import admin
from django.urls import reverse
# Register your models here.
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image','price', 'stock',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price',  'image','stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    
admin.site.register(Product, ProductAdmin)