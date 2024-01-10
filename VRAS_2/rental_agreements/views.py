# rental_agreements/views.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from django.urls import reverse_lazy
from .models import RentalAgreement

class RentalAgreementListView(ListView):
    model = RentalAgreement
    template_name = 'rental_agreement_list.html'

class RentalAgreementDetailView(DetailView):
    model = RentalAgreement
    template_name = 'rental_agreement_detail.html'

class RentalAgreementCreateView(CreateView):
    model = RentalAgreement
    template_name = 'rental_agreement_form.html'
    fields = ['customer', 'vehicle', 'start_date', 'end_date', 'rental_cost']

class RentalAgreementUpdateView(UpdateView):
    model = RentalAgreement
    template_name = 'rental_agreement_form.html'
    fields = ['customer', 'vehicle', 'start_date', 'end_date', 'rental_cost']

class ReceiptView(TemplateView):
    template_name = 'receipt.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rental_agreement'] = RentalAgreement.objects.get(pk=self.kwargs['pk'])
        return context
