import subprocess

from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


def network(request):
    # 'wlan0' for RPi and 'wlp5s0' for my laptop
    result_of_iwconfig = subprocess.run(['iwconfig', 'wlan0'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    result_of_ifconfig = subprocess.run(['ifconfig', 'eth0'], stdout=subprocess.PIPE).stdout.decode('utf-8')

    list_with_iwconfig_data = result_of_iwconfig.split('\n')
    list_with_ifconfig_data = result_of_ifconfig.split('\n')

    network_dict = {}

    for item in list_with_iwconfig_data:
        if 'SSID' in item:
            network_dict['name'] = item[item.find('\"')+1: item.rfind('\"')]
        if 'Frequency' in item:
            network_dict['Frequency'] = item[item.find('Frequency')+10: item.rfind('Hz')+2]
        if 'Rate' in item:
            network_dict['BitRate'] = item[item.find('Rate')+5: item.rfind('b/s')+3]
        if 'Quality' in item:
            network_dict['LinkQuality'] = item[item.find('Quality')+8: item.find('=')+6]

    for item in list_with_ifconfig_data:
        if 'broadcast' in item:
            network_dict['wired_ip'] = item[item.find('inet')+4: item.rfind('netmask')-1]
        return render(request, 'network.html', {'network_dict': network_dict})


def updates(request):
    return render(request, 'updates.html')
