from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

class Device(models.Model):
    hostname = models.CharField(max_length=20)
    macAddress = models.CharField(max_length=17)
    ipAddress = models.GenericIPAddressField(protocol='both', unpack_ipv4=True)
    serialNumber = models.CharField(max_length=16)
    role = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    PRINTER = 'PRT'
    PLC = 'PLC'
    SECURITYCAMERA = 'SC'

    TYPE_CATEGORY_CHOICES = [
        (PRINTER, 'printer'),
        (PLC, 'plc'),
        (SECURITYCAMERA, 'security camera'),
    ]
    type_category = models.CharField(max_length=15, choices=TYPE_CATEGORY_CHOICES)

    #location = models.TextField(blank=True) #probably need to change to a FormField
    location = models.ForeignKey('Location', related_name='devices', on_delete=models.CASCADE)
    notes = models.TextField(blank=True) #not mandatory
    user = models.ForeignKey(User, related_name='devices', on_delete=models.CASCADE)
    floor = models.IntegerField(validators=[MinValueValidator(limit_value=1)])

    def clean(self):
        super().clean()
        if self.floor > self.location.number_floors:
            raise ValidationError('Invalid floor number') #check how to add proper validation errors

    def __str__(self):
        return self.hostname

class Location(models.Model):
    address = models.CharField(max_length=50)
    building = models.CharField(max_length=50)
    number_floors = models.IntegerField(validators=[MinValueValidator(limit_value=1)])

    def __str__(self):
        return self.building + " " + self.address

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
