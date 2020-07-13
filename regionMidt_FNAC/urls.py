"""regionMidt_FNAC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from device import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),

    # Devices
    path('', views.home, name='home'),
    path('create/', views.createdevice, name='createdevice'),
    #path('current/', views.currentdevices, name='currentdevices'),
    path('current/', views.CurrentdevicesView.as_view(), name='currentdevices'),
    path('device/<int:device_pk>', views.viewdevice, name='viewdevice'),
    #path('device/<int:pk>', views.DeviceView.as_view(), name='viewdevice'),
    path('device/<int:device_pk>/delete', views.deletedevice, name='deletedevice'),
]
