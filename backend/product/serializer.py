from .models import Category,Product
from rest_framework import serializers



class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Category
        fields="__all__"
    
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Product
        fields="__all__"
        read_only_fields=['id']