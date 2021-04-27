from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def services(request):
    return render(request, 'app/services.html')

def store(request):
    return render(request, 'app/store.html')

def blog(request):
    return render(request, 'app/blog.html')

def contacts(request):
    return render(request, 'app/contacts.html')