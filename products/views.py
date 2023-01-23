from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import ProductCategory, Product, Basket


def index(request):
    context = {
        'title': 'Store',
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


def category_detail(request, cat_id):
    context = {
        'title': f'Store - {ProductCategory.objects.get(pk=cat_id)}',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.filter(category_id=cat_id),
        'cat_selected': cat_id,
    }
    return render(request, 'products/category_detail.html', context)
