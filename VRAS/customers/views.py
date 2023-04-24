from django.views.generic import ListView, UpdateView
from django.urls import reverse_lazy
from .forms import EditCustomerForm
from .models import Customer


class CustomerView(ListView):
    model = Customer
    template_name = 'customer_list.html'


class EditCustomerView(UpdateView):
    model = Customer
    form_class = EditCustomerForm
    template_name = 'update_customer.html'
    success_url = reverse_lazy('customer_list')
