from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    title=models.CharField(null=False,max_length=200)
    price=models.FloatField(default=0)
    description=models.TextField()

    def __str__(self):
        return self.title


