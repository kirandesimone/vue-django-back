from dataclasses import fields
from os import name
from django.contrib import admin
from .models import Product, Post

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created', 'product')
    list_filter = ('author',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Post, PostAdmin)
