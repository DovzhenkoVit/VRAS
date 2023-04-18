from django.views.generic import ListView
from .models import Vehicle


class VehicleView(ListView):
    model = Vehicle
    template_name = "vehicle_list.html"
