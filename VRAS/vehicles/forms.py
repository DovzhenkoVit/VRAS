from django import forms
from .models import Vehicle


class AddVehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'


class EditVehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
