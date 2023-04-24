from django.views.generic import ListView, UpdateView
from django.urls import reverse_lazy
from .models import Vehicle
from .forms import EditVehicleForm


class VehicleView(ListView):
    model = Vehicle
    template_name = 'vehicle_list.html'


class EditVehicleView(UpdateView):
    model = Vehicle
    form_class = EditVehicleForm
    template_name = 'update_vehicle.html'
    success_url = reverse_lazy('vehicle_list')
