from django.views.generic import ListView, CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy
from .forms import AddCustomerForm, EditCustomerForm
from .models import Customer


class CustomerView(ListView):
    model = Customer
    template_name = 'customer_list.html'


class AddCustomerView(CreateView):
    model = Customer
    template_name = 'add_customer.html'
    form_class = AddCustomerForm


class EditCustomerView(UpdateView):
    model = Customer
    form_class = EditCustomerForm
    template_name = 'update_customer.html'


class DeleteCustomerView(DeleteView):
    model = Customer
    template_name = 'delete_customer.html'
    success_url = reverse_lazy('customer_list')
