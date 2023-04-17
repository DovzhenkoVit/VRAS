from django.db import models

# Create your models here.


class Vehicle(models.Model):
    car_brand = models.CharField(max_length=64)

    model = models.CharField(max_length=64)

    year = models.IntegerField()

    licence_plate = models.CharField(max_length=8)

    rental_rate = models.IntegerField()

    def __str__(self):
        return self.car_brand + self.model
