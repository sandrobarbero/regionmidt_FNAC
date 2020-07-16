from django import forms
from django.forms import ModelForm
from .models import Device

class DeviceForm(ModelForm):
    #error_css_class = 'is_invalid'
    #required_css_class = 'required'

    class Meta:
        model = Device
        fields = ['hostname', 'mac_Address', 'ip_Address', 'serial_Number', 'role', 'type_or_category', 'location', 'notes', 'floor']
        widgets = {
            'hostname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Max 20 chars'}),
            'mac_Address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Format: aa:bb:cc:dd:ee:ff'}),
            'ip_Address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Format: x.w.y.z'}),
            'serial_Number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Max 16 chars'}),
            'role': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Max 20 chars'}),
            'type_or_category': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
            'floor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Minimum Value = 0'}),
        }
