from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import DeviceForm
from .models import Device
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views import generic
#from django.views.generic.detail import DetailView
#from django.views.generic.list import ListView
#from django.views.generic.edit import FormMixin, FormView

def home(request):
    return render(request, 'device/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'device/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currentdevices')
            except IntegrityError:
                return render(request, 'device/signupuser.html', {'form':UserCreationForm(), 'error': 'This user already taken. Please choose another username'})

        else:
            return render(request, 'device/signupuser.html', {'form':UserCreationForm(), 'error': 'Password mismatch'})

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'device/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'device/loginuser.html', {'form':AuthenticationForm(), 'error': ' Username and password did not match'})
        else:
            login(request, user)
            return redirect('currentdevices')


'''@login_required
def createdevice(request):
    if request.method == 'GET':
        return render(request, 'device/createdevice.html', {'form':DeviceForm()})
    else:
        try:
            form = DeviceForm(request.POST)
            form.instance.user = request.user # add user info for the new device
            newdevice = form.save(commit=True) # not to save in the DB
            # newdevice.user = request.user # add user info for the new device
            # newdevice.save() # finally save it in the DB
            return redirect('currentdevices')
        except ValueError:
            return render(request, 'device/createdevice.html', {'form':form, 'error': 'Bad data passed in. Try again'})'''

class CreatedeviceView(generic.CreateView):
    model = Device
    template_name = 'device/createdevice.html'
    context_object_name = 'device'
    form_class = DeviceForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    '''def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user.pk
        return initial'''

    def get_success_url(self):
        return reverse('viewdevice', kwargs={'pk': self.object.pk})

'''@login_required
def currentdevices(request):
    #devices = Device.objects.filter(user=request.user)
    devices = request.user.devices.all()
    return render(request, 'device/currentdevices.html', {'devices':devices})'''

class CurrentdevicesView(generic.ListView):
    model = Device
    template_name = 'device/currentdevices.html'
    context_object_name = 'devices'


'''@login_required
def viewdevice(request, device_pk):
    #device = get_object_or_404(Device, pk=device_pk, user=request.user) #user restriction
    device = get_object_or_404(Device, pk=device_pk)
    if request.method == 'GET':
        form = DeviceForm(instance=device)
        return render(request, 'device/viewdevice.html', {'device':device, 'form':form})
    else:
        try:
            form = DeviceForm(request.POST, instance=device)
            form.save()
            return redirect('currentdevices')
        except ValueError:
            return render(request, 'device/viewdevice.html', {'device':device, 'form':form, ' error': 'Bad info'})'''

class DeviceView(generic.DetailView):
    model = Device
    template_name = 'device/viewdevice.html'
    context_object_name = 'device'
    form_class = DeviceForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DeviceForm(instance=self.object)
        #context['form'].fields.widget.attrs['readonly'] = True
        #context['form'] = DeviceForm(instance=context['device'])
        return context

class UpdateDeviceView(generic.UpdateView):
    model = Device
    template_name = 'device/updatedevice.html'
    context_object_name = 'device'
    form_class = DeviceForm

    def get_success_url(self):
        return reverse('viewdevice', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

'''@login_required
def deletedevice(request, device_pk):
    device = get_object_or_404(Device, pk=device_pk, user=request.user)
    if request.method == 'POST':
        device.delete()
        return redirect('currentdevices')'''

class DeleteDeviceView(generic.DeleteView):
    model = Device
    template_name = 'device/deletedevice.html'
    success_url = reverse_lazy('currentdevices')
