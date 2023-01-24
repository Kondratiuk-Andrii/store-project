from django.urls import path
from .views import *

app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    path('page/<int:page>/', ProductsListView.as_view(), name='paginator'),
    path('<slug:category_slug>/', ProductsListView.as_view(), name='category'),
    path('<slug:category_slug>/page/<int:page>/', ProductsListView.as_view(), name='category_paginator'),

    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),

]
