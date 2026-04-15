from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    id=models.IntegerField(auto_created=True,primary_key=True)
    title=models.CharField(null=False,max_length=200)
    price=models.FloatField(default=0)
    description=models.TextField(blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    discount=models.IntegerField(default=0)
    
    @property

    
    def final_price(self):
        return self.price-(self.discount*0.01*self.price)


    def __str__(self):
        return self.title

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.user}"

class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Cartitems- {self.product.title} x {self.quantity}"
    @property
    def total_price(self):
        return self.product.price*self.quantity

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    status=models.CharField(max_length=50)

    def __str__(self):
        return f"Order- {self.user}"

   

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    discount=models.IntegerField(default=0)

    def __str__(self):
        return f"Orderitems- {self.product.title} x {self.quantity}"
    
    @property


    def total_price(self):
        return self.product.price*self.quantity
    
    def final_price(self):
        return self.total_price-(self.discount*0.01*self.total_price)
    
    




