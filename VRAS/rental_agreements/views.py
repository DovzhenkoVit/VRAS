from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import RentalAgreement
from .forms import AddRentalAgreementForm, EditRentalAgreementForm

# Create your views here.


class RentalAgreementView(ListView):
    model = RentalAgreement
    template_name = 'rental_agreement_list.html'


class AddRentalAgreementView(CreateView):
    model = RentalAgreement
    template_name = 'add_rental_agreement.html'
    form_class = AddRentalAgreementForm


class EditRentalAgreementView(UpdateView):
    model = RentalAgreement
    template_name = 'update_rental_agreement.html'
    form_class = EditRentalAgreementForm


class DeleteRentalAgreementView(DeleteView):
    model = RentalAgreement
    template_name = 'delete_rental_agreement.html'
    success_url = reverse_lazy('rental_agreement_list')
