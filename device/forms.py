from django.forms import ModelForm
from .models import Device

class DeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = ['hostname', 'mac_Address', 'ip_Address', 'serial_Number', 'role', 'type_or_category', 'location', 'notes', 'floor']
