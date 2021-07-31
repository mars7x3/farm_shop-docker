from django.urls import path

from product.views import *


urlpatterns = [
    path('', ContentView.as_view(), name='home'),
    path('products/', ProductListView.as_view(), name='products'),
    path('product/<int:product_id>/', ProductDetailView.as_view(), name='detail'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('order/create/', OrderCreateView.as_view(), name='order_create')
]


