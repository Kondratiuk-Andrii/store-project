from django.db.models import Count
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import ProductCategory, Product, Basket


def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', context)


def products(request, category_slug=None, page_number=1):
    products = Product.objects.filter(category__slug=category_slug) if category_slug else Product.objects.filter()
    per_page = 3
    paginator = Paginator(products, per_page=per_page)
    products_paginator = paginator.page(page_number)
    context = {
        'title': 'Store - Каталог',
        'categories': ProductCategory.objects.annotate(total=Count('product')).filter(total__gt=0),
        'products': products_paginator,
        'category_slug': category_slug,
    }
    return render(request, 'products/products.html', context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return redirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return redirect(request.META['HTTP_REFERER'])
