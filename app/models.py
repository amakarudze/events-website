"""
Definition of models.
"""

from django.db import models
import datetime
 

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=120)
    shortdesc = models.CharField(max_length=120)
    description = models.CharField(max_length=255)
    photo = models.CharField(max_length=255)

    class Meta:
        managed = True

    def get_providers(self):
       return Category.objects.all()

    def __str__(self):
        return self.category
         


class Provider(models.Model):
    name = models.SlugField(max_length=120)
    shortdesc = models.CharField(max_length=120)
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=120)    
    prices = models.CharField(max_length=150)
    photo = models.CharField(max_length=255)
    photo1 = models.CharField(max_length=255)
    photo2 = models.CharField(max_length=255)
    category = models.ForeignKey(Category)

    class Meta:
        managed = True

    def __str__(self):
        return self.name

class ServiceProvider(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=120)
    shortdesc = models.CharField(max_length=120)
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=120)    
    prices = models.CharField(max_length=150)
    photo = models.CharField(max_length=255)
    photo1 = models.CharField(max_length=255)
    photo2 = models.CharField(max_length=255)
    category = models.ForeignKey(Category)

    class Meta:
        managed = True

    def __str__(self):
        return self.name

    

class Order(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)
    servicerequired = models.CharField("service required", max_length=120)
    details = models.TextField()
    eventdate = models.DateTimeField("event date")
    orderdate = models.DateTimeField(auto_now_add=True)
    serviceprovider = models.ForeignKey(ServiceProvider)




class Contact(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=120)
    subject = models.CharField(max_length=120)
    provider = models.ForeignKey(ServiceProvider)
    message = models.TextField()
    emaildate = models.DateTimeField(auto_now_add=True)
    

