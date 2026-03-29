from django.db import models

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
    def total_price(self):
        return self.price-(self.discount*0.01*self.price)


    def __str__(self):
        return self.title


