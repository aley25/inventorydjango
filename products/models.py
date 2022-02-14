from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
    title = models.CharField(max_length=75)
    slug = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)



class Product(models.Model):
    title = models.CharField(max_length=75)
    summary = models.CharField(max_length=50)
    type = models.SmallIntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

class Product_Meta(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    key = models.CharField(max_length=25)
    content = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class Product_Category(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)



class Brand(models.Model):
    title = models.CharField(max_length=75)
    summary = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)








