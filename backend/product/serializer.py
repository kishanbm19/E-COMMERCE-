from .models import Category,Product
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