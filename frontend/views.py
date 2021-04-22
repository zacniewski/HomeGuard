import subprocess

from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


def network(request):
    # list_files = subprocess.run(["ls", "-l"])
    return render(request, 'network.html')


def updates(request):
    return render(request, 'updates.html')
