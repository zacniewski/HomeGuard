from django.shortcuts import render


def camera_usb(request):
    return render(request, 'vision/camera-usb.html')