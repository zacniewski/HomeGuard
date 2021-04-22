import subprocess

from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


def network(request):
    result_of_iwconfig = subprocess.run(['iwconfig', 'wlp5s0'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    list_with_iwconfig_data = result_of_iwconfig.split('\n')
    iwconfig_dict = {}
    for item in list_with_iwconfig_data:
        print(item.strip().split(' '))
    return render(request, 'network.html')


def updates(request):
    return render(request, 'updates.html')
