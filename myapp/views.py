from itertools import product
from pickle import GET
from turtle import pos
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Product, Post
from myapp.serializers.serialize import ProductSerializer, PostSerializer
# Create your views here.
@csrf_exempt
def all_products(request):
    if request.method == "GET":
        products = Product.objects.all()
        serialize = ProductSerializer(products, many=True)
        return JsonResponse(serialize.data, safe=False)




###Retreiving Posts

@csrf_exempt
def all_posts(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serialize = PostSerializer(posts, many=True)
        return JsonResponse(serialize.data, safe=False)

@csrf_exempt
def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "GET":
        serialize = PostSerializer(post)
        return JsonResponse(serialize.data)



