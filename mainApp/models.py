from django.db import models

# Create your models here.

class SellCar(models.Model):
    image = models.ImageField(upload_to='sellcars')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    carType = models.CharField(max_length=50)
    carCompany = models.CharField(max_length=100)
    carName = models.CharField(max_length=50)
    carModel = models.CharField(max_length=50)
    mileage = models.CharField(max_length=10)
    color = models.CharField(max_length=20)
    kmDriven = models.CharField(max_length=20)
    price = models.CharField(max_length=50)
    description = models.TextField()
    

class AddCar(models.Model):
    image = models.ImageField(upload_to='addcars')
    carType = models.CharField(max_length=50)
    carCompany = models.CharField(max_length=100)
    carName = models.CharField(max_length=50)
    carModel = models.CharField(max_length=50)
    mileage = models.CharField(max_length=10)
    color = models.CharField(max_length=20)
    kmDriven = models.CharField(max_length=20)
    price = models.CharField(max_length=50)
    description = models.TextField()


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    message = models.TextField()
