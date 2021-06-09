from django.db import models
from .models import Product
from django.contrib.auth.models import User
import datetime

class Order(models.Model):
    productname = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.CharField(max_length=50)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    datetime = models.DateField( default=datetime.datetime.now)
    address = models.CharField(max_length=200)
    mobilno = models.CharField(max_length=20)
    confirm = models.CharField( max_length=50 , default="paid")




    