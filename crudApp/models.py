from django.db import models
from django.contrib.auth.models import User


class TravelPlanet(models.Model):
    hotel = models.CharField(max_length=100)
    arrival = models.DateField(auto_now=False, auto_now_add=False)
    departure = models.DateField(auto_now=False, auto_now_add=False)
    guests = models.PositiveIntegerField()
    price = models.PositiveIntegerField()


class Product(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    image = models.ImageField(upload_to="Product Image")


class Customer(models.Model):

    name = models.CharField(max_length=100)
    gander = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    phone_num = models.PositiveIntegerField()
    email = models.EmailField(max_length=254)
    facebook = models.CharField(max_length=100)
    image = models.ImageField(upload_to="Profile Picture/",
                              default='default/default.png', blank=True, null=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    t_name = models.CharField(max_length=50)


class Student(models.Model):
    user = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    s_name = models.ImageField(
        upload_to="None", height_field=None, width_field=None, max_length=None)
