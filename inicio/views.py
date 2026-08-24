from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def v1_inicio(request):
    return HttpResponse("<h1>Vista 1 inicio</h1>")

