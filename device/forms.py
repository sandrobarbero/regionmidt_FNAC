from django.forms import ModelForm
from .models import Device

class DeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = ['hostname', 'macAddress', 'ipAddress', 'serialNumber', 'role', 'type_category', 'location', 'notes', 'floor']
