from django.urls import path
from .views import IndexView, network, updates, update_system

app_name = 'frontend'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('network/', network, name='network'),
    path('updates/', updates, name='updates'),
    path('update-system-confirmed/', update_system, name='update_system')
]
