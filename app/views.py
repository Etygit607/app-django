from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def store(request):
    return render(request, 'app/store.html')
