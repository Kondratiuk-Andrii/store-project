from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.db.models import Count
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from products.models import ProductCategory, Product, Basket


class IndexView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Store'
        return context


class ProductsListView(ListView):
    template_name = 'products/products.html'
    model = Product
    paginate_by = 3

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_slug = self.kwargs.get('category_slug')
        return queryset.filter(category__slug=category_slug) if category_slug else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Store - Каталог'
        context['categories'] = ProductCategory.objects.annotate(total=Count('product')).filter(total__gt=0)
        context['category_slug'] = self.kwargs.get('category_slug')
        return context


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
