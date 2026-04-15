from .models import Category,Product,Cart,CartItem,Order,OrderItem
from rest_framework import serializers



class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Category
        fields="__all__"
    
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    final_price=serializers.ReadOnlyField()
    class Meta:
        model=Product
        fields=['url','id','title','description','price','discount','final_price','category']
        read_only_fields=['id']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields="__all__"
        

class CartItemSerializer(serializers.ModelSerializer):
    total_price=serializers.ReadOnlyField()
    Item = serializers.CharField(source='product.title', read_only=True)
    class Meta:
        model=CartItem
        fields=['cart','product','Item','quantity','total_price']
        
       

class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Order
        fields="__all__"
        

class OrderItemSerializer(serializers.ModelSerializer):
    total_price=serializers.ReadOnlyField()
    final_price=serializers.ReadOnlyField()
    Item=serializers.CharField(source='product.title',read_only=True)
    class Meta:
        model=OrderItem
        fields=['order','product','Item','quantity','total_price','discount','final_price']
        read_only_fields=['total_price','final_price']
        write_only_fields=['product']