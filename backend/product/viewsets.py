from django.shortcuts import render
from rest_framework import viewsets
from .serializer import CategorySerializer,ProductSerializer
from .models import Category,Product

# Create your views here.

class Categoryviewset(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class Productviewset(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer



