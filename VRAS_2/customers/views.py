# customers/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Customer

class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'

class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customer_form.html'
    fields = ['first_name', 'last_name', 'address', 'email', 'phone_number']

class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customer_form.html'
    fields = ['first_name', 'last_name', 'address', 'email', 'phone_number']

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer_confirm_delete.html'
    success_url = reverse_lazy('customer-list')
