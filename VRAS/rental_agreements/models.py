from django.db import models
from vehicles.models import Vehicle
from customers.models import Customer

# Create your models here.


class RentalAgreement(models.Model):
    rental_duration = models.DurationField()

    rental_fee = models.IntegerField()

    is_paid = models.BooleanField(default=False)

    payment_receipt = models.FileField(null=True, blank=True)

    vehicle = models.ForeignKey(Vehicle, null=True, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
