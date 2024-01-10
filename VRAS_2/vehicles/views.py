# vehicles/views.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Vehicle

class VehicleListView(ListView):
    model = Vehicle
    template_name = 'vehicle_list.html'

class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = 'vehicle_detail.html'

class VehicleCreateView(CreateView):
    model = Vehicle
    template_name = 'vehicle_form.html'
    fields = ['manufacturer', 'model', 'year', 'license_plate', 'rental_cost']

class VehicleUpdateView(UpdateView):
    model = Vehicle
    template_name = 'vehicle_form.html'
    fields = ['manufacturer', 'model', 'year', 'license_plate', 'rental_cost']

class VehicleDeleteView(DeleteView):
    model = Vehicle
    template_name = 'vehicle_confirm_delete.html'
    success_url = reverse_lazy('vehicle-list')

