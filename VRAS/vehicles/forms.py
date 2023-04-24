from django import forms
from .models import Vehicle


class EditVehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
