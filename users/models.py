from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class User(models.Model):
    firstName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50)
    firstLastName = models.CharField(max_length=50)
    secondLastName = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    mobile = models.CharField(max_length=25)
    email = models.EmailField(max_length=150)
    # i need to create after
    #passwordHash = 
    lastLogin = models.DateTimeField(auto_now=True)
    registeredAt = models.DateTimeField(auto_now=True)


