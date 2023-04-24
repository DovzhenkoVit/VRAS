from django import forms
from .models import Customer


class AddCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class EditCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
