from .models import Category,Product,Cart,CartItem,Order,OrderItem
from rest_framework import serializers



class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Category
        fields="__all__"
    
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    total_price=serializers.ReadOnlyField()
    class Meta:
        model=Product
        fields=['url','id','title','description','price','discount','total_price','category']
        read_only_fields=['id']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields="__all__"

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartItem
        fields="__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields="__all__"

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields="__all__"