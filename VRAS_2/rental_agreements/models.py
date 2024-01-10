# rental_agreements/models.py
from django.db import models
from customers.models import Customer
from vehicles.models import Vehicle

class RentalAgreement(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    rental_cost = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Rental Agreement #{self.pk} - {self.customer} - {self.vehicle}"
