from django.urls import path
from django.views.generic import TemplateView
from .views import camera_usb_streaming

app_name = "vision"
urlpatterns = [
    path("camera-usb-streaming/", camera_usb_streaming, name="camera_usb_streaming"),

    path("camera-usb-iframe/", TemplateView.as_view(template_name="camera-usb.html"),
         name='camera_usb_iframe'),
    ]
