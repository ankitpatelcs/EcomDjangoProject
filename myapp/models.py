
from tkinter import CASCADE
from django.db import models
from seller.models import Product

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    mobile=models.CharField(max_length=50)
    address=models.TextField(null=True,blank=True)
    password=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name


class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField()
    pay_id = models.CharField(max_length=20)
    verify = models.BooleanField(default=False)
    order_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.name)

class OrderDetails(models.Model):

    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField()
    order = models.ForeignKey(Order,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.order.id)