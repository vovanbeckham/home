

from django import forms

from home.models import Sensor


class EditDeviceForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = '__all__'