from django.urls import path
from .views import camera_usb, test_usb_camera

app_name = "vision"
urlpatterns = [
    path("camera-usb/", camera_usb, name="camera_usb"),
]
