from django.db import models
from django.contrib.auth.models import User

class Product(models.Model) :
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.code + ', ' + self.name + ', ' + self.description

class Client(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

class User(models.Model) :
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Sale(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # client =
    # saleDetails =
    date = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(null=True, blank=True)

class SaleDetail(models.Model) :
    # product =
    quantity = models.IntegerField(null=True, blank=True)
    # subtotal = 