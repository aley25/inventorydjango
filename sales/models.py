from django.core.exceptions import DisallowedRedirect
from django.db import models
from django.db.models.deletion import CASCADE, RESTRICT
from django.db.models.fields import SmallIntegerField
from django.db.models.fields.related import OneToOneField
from inventory.settings import TIME_ZONE
from products.models import Category,Product, Brand
from users.models import Role, User
from django.utils.timezone import *
# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete= models.RESTRICT)
    type = models.SmallIntegerField()
    status = models.SmallIntegerField()
    subTotal = models.FloatField()
    itemDiscount = models.FloatField()
    tax = models.FloatField()
    shipping = models.FloatField()
    total = models.FloatField()
    promo = models.CharField(max_length=50)
    discount = models.FloatField()
    grandTotal = models.FloatField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    

class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=RESTRICT)
    brand = models.ForeignKey(Brand, on_delete=models.RESTRICT)
    supplier = models.ForeignKey(User, on_delete=models.RESTRICT)
    order = models.ForeignKey(Order, on_delete=RESTRICT)
    sku = models.CharField(max_length=100)
    mrp = models.FloatField()
    discount = models.FloatField()
    price = models.FloatField()
    quantity = models.SmallIntegerField()
    sold = models.SmallIntegerField()
    available = SmallIntegerField()
    defective = SmallIntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class Order_Item(models.Model):
    product = models.ForeignKey(Product, on_delete=RESTRICT)
    item = models.ForeignKey(Item, on_delete=RESTRICT)
    order = models.ForeignKey(Order, on_delete=RESTRICT)
    sku = models.CharField(max_length=100)
    price = models.FloatField()
    discount = models.FloatField()
    quantity = models.SmallIntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)



class Address(models.Model):
    user = models.ForeignKey(User, on_delete=RESTRICT)
    order = models.ForeignKey(Order, on_delete=RESTRICT)
    firstName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    line1 = models.CharField(max_length=50)
    line2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=RESTRICT)
    order = models.ForeignKey(Order, on_delete=RESTRICT)
    code = models.CharField(max_length=100)
    type = models.SmallIntegerField()
    mode = models.SmallIntegerField()
    status = models.SmallIntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
