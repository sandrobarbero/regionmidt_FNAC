from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import DeviceForm
from .models import Device
from django.utils import timezone
from django.contrib.auth.decorators import login_required

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
                return redirect('home') #need to verify!
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
            return redirect('home')
            #return redirect('createdevice')


@login_required
def createdevice(request):
    if request.method == 'GET':
        return render(request, 'device/createdevice.html', {'form':DeviceForm()})
    else:
        try:
            form = DeviceForm(request.POST)
            newdevice = form.save(commit=False) # to not save in the DB
            newdevice.user = request.user # add user info for the new todo
            newdevice.save() # finally save it in the DB
            #return render(request, 'todo/currenttodos.html')
            return redirect('home') # need to check!
            #return redirect('currentdevices')
        except ValueError:
            return render(request, 'device/createdevice.html', {'form':DeviceForm(), 'error': 'Bad data passed in. Try again'})

@login_required
def currentdevices(request):
    #devices = Device.objects.filter(user=request.user)
    devices = request.user.devices.all()
    return render(request, 'device/currentdevices.html', {'devices':devices})

@login_required
def viewdevice(request, device_pk):
    device = get_object_or_404(Device, pk=device_pk, user=request.user)
    if request.method == 'GET':
        form = DeviceForm(instance=device)
        return render(request, 'device/viewdevice.html', {'device':device, 'form':form})
    else:
        try:
            form = DeviceForm(request.POST, instance=device)
            form.save()
            return redirect('currentdevices')
        except ValueError:
            return render(request, 'device/viewdevice.html', {'device':device, 'form':form, ' error': 'Bad info'})

@login_required
def deletedevice(request, device_pk):
    device = get_object_or_404(Device, pk=device_pk, user=request.user)
    if request.method == 'POST':
        device.delete()
        return redirect('currentdevices')
