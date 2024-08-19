# monitor/urls.py

from django.urls import path
from .views import monitor_file, get_latest_lines

urlpatterns = [
    path('', monitor_file, name='monitor_file'),
    path('get-latest-lines/', get_latest_lines, name='get_latest_lines'),
]
