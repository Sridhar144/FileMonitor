# monitor/routing.py

from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/monitor/', consumers.FileMonitorConsumer.as_asgi()),
]
