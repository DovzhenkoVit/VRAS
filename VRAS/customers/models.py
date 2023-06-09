from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=64)

    surname = models.CharField(max_length=64)

    adress = models.CharField(max_length=255)

    phone_number = models.IntegerField()

    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.name} {self.surname}"