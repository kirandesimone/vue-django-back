from django import urls, views
from django.urls import path
from myapp import views

urlpatterns= [
    path('api/v1/products/', views.all_products),
    path('api/v1/posts/', views.all_posts),
    path('api/v1/posts/<id>', views.post_detail),
]