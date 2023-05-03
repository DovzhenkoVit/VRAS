from django import forms
from .models import RentalAgreement


class AddRentalAgreementForm(forms.ModelForm):
    class Meta:
        model = RentalAgreement
        fields = '__all__'


class EditRentalAgreementForm(forms.ModelForm):
    class Meta:
        model = RentalAgreement
        fields = '__all__'
