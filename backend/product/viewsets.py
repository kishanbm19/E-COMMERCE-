from django.shortcuts import render
from rest_framework import viewsets
from .serializer import CategorySerializer,ProductSerializer,CartSerializer,CartItemSerializer,OrderItemSerializer,OrderSerializer
from .models import Category,Product,Cart,CartItem,Order,OrderItem

# Create your views here.

class Categoryviewset(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class Productviewset(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class Cartview(viewsets.ModelViewSet):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer

class CartItemview(viewsets.ModelViewSet):
    queryset=CartItem.objects.all()
    serializer_class=CartItemSerializer

class Orderview(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer

class OrderItemview(viewsets.ModelViewSet):
    queryset=OrderItem.objects.all()
    serializer_class=OrderItemSerializer

    

