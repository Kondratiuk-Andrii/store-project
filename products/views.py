from django.shortcuts import render
from .models import *


def index(request):
    context = {
        'title': 'Store',
        'is_promotion': False,
        'cat_selected': 0,
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
        'cat_selected': 0,
    }
    return render(request, 'products/products.html', context)


def category_detail(request, cat_id):
    context = {
        'title': f'Store - {ProductCategory.objects.get(pk=cat_id)}',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.filter(category_id=cat_id),
        'cat_selected': cat_id,
    }
    return render(request, 'products/category_detail.html', context)
