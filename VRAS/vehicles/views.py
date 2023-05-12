from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Vehicle
from .forms import AddVehicleForm, EditVehicleForm


class VehicleView(ListView):
    model = Vehicle
    template_name = 'vehicle_list.html'


class AddVehicleView(CreateView):
    model = Vehicle
    form_class = AddVehicleForm
    template_name = 'add_vehicle.html'


class EditVehicleView(UpdateView):
    model = Vehicle
    form_class = EditVehicleForm
    template_name = 'update_vehicle.html'


class DeleteVehicleView(DeleteView):
    model = Vehicle
    template_name = 'delete_vehicle.html'
    success_url = reverse_lazy('vehicle_list')
