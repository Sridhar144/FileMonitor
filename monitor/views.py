# monitor/views.py

from django.shortcuts import render
from django.http import JsonResponse

def monitor_file(request):
    return render(request, 'monitor/monitor_file.html')

file_path = "monitor/example.log"

def get_latest_lines(request):
    lines = []
    with open(file_path, 'r') as f:
        lines = f.readlines()[-10:]  # Get the last 10 lines
    return JsonResponse({"lines": lines})