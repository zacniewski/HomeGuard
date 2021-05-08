from django.urls import path
from .views import camera_usb, test_usb_camera

app_name = "vision"
urlpatterns = [
    path("camera-usb/", test_usb_camera, name="camera_usb"),
]
