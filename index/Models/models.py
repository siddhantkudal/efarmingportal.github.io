from django.db import models
from .category import Category
# Create your models here.
class Product(models.Model):
    productname = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    climatecondition = models.CharField(max_length=100)
    weight = models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.ImageField(upload_to='uploaded/images')
    def __str__(self):
        return self.productname