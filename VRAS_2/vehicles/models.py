# vehicles/models.py
from django.db import models

class Vehicle(models.Model):
    manufacturer = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    license_plate = models.CharField(max_length=20)
    rental_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.manufacturer} {self.model} ({self.year})"
