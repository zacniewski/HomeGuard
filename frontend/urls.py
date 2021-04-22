from django.urls import path
from .views import IndexView, network, updates

app_name = 'frontend'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('network/', network, name='network'),
    path('updates/', updates, name='updates'),
]
