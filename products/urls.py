from django.urls import path
from .views import *

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('<int:cat_id>/', category_detail, name='category_detail'),
]
