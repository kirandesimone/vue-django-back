from tkinter import CASCADE
from django.db import models
from django.forms import DateTimeField

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)

    @classmethod
    def create(cls, name):
        product = cls(name=name)
        return product
    
    def __str__(self):
        return self.name


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    slug = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

