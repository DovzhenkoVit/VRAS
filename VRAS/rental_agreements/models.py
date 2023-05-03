from django.db import models
from django.urls import reverse
from vehicles.models import Vehicle
from customers.models import Customer

# Create your models here.


class RentalAgreement(models.Model):
    rental_start_date = models.DateField(null=True)

    rental_end_date = models.DateField(null=True)

    rental_fee = models.IntegerField()

    is_paid = models.BooleanField(default=False)

    payment_receipt = models.FileField(null=True, blank=True)

    vehicle = models.ForeignKey(Vehicle, null=True, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer} {self.vehicle} {self.rental_start_date}"

    def get_absolute_url(self):
        return reverse('rental_agreement_list')
