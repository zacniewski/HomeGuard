import subprocess

from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


def network(request):
    # 'wlan0' for RPi and 'wlp5s0' for my laptop
    result_of_iwconfig = subprocess.run(['iwconfig', 'wlp5s0'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    result_of_ifconfig = subprocess.run(['ifconfig', 'wlp5s0'], stdout=subprocess.PIPE).stdout.decode('utf-8')

    list_with_iwconfig_data = result_of_iwconfig.split('\n')
    iwconfig_dict = {}
    for item in list_with_iwconfig_data:
        if 'SSID' in item:
            iwconfig_dict['name'] = item[item.find('\"')+1: item.rfind('\"')]
        if 'Frequency' in item:
            iwconfig_dict['Frequency'] = item[item.find('Frequency')+10: item.rfind('Hz')+2]
        if 'Rate' in item:
            iwconfig_dict['BitRate'] = item[item.find('Rate')+5: item.rfind('b/s')+3]
        if 'Quality' in item:
            iwconfig_dict['LinkQuality'] = item[item.find('Quality')+8: item.find('=')+6]
        print(item.strip())
    print(iwconfig_dict)
    return render(request, 'network.html', {'iwconfig_dict': iwconfig_dict})


def updates(request):
    return render(request, 'updates.html')
