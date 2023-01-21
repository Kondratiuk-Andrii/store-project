from django.urls import path
from .views import *

app_name = 'products'

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),
    path('products/<int:cat_id>', category_detail, name='category_detail'),
]
