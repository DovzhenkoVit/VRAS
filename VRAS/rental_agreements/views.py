import io
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, TemplateView
from django.http import FileResponse, HttpResponse
from django.urls import reverse_lazy
from django.template import loader

from .models import RentalAgreement
from .forms import AddRentalAgreementForm, EditRentalAgreementForm

from reportlab.pdfgen import canvas


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


class InvoiceView(View):
    def get(self, request, pk):


        invoice = RentalAgreement.objects.filter(pk=pk)
        print(invoice)
        template = loader.get_template('invoice.html')
        context = {
            'rental_agreements': invoice,
        }
        return HttpResponse(template.render(context, request))
