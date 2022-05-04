from django.db import models

# Create your models here.

class SellerUser(models.Model):

    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=50)
    verify = models.BooleanField(default=False)
    password = models.CharField(max_length=20,null=True,blank=True)
    pic = models.FileField(upload_to='seller profile',default='avtar.png')

    def __str__(self):
        return self.fname


class Product(models.Model):

    seller = models.ForeignKey(SellerUser,on_delete=models.CASCADE)  # Foreignkey
    name = models.CharField(max_length=50)
    des = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField(default=0)
    pic = models.FileField(upload_to='products',default='avatar.png')
    discount = models.IntegerField()

    def __str__(self):
        return self.name