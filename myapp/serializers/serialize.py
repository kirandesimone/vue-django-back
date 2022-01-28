from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from ..models import Product, Post

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id', 
            'title', 
            'created', 
            'slug',
            'author',
            'content',
            'product'
        ]