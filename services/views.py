from django.shortcuts import render, HttpResponse
from services.models import Service

# Create your views here.

def services(request):
    services = Service.objects.all()
    return render(request, 'app/services.html',{"services":services})