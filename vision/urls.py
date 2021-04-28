from django.urls import path
from .views import camera_usb

app_name = 'vision'
urlpatterns = [
    path('camera-usb/', camera_usb, name='camera_usb'),
]
