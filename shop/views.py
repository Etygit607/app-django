from django.shortcuts import render, HttpResponse
from .models import Product

# Create your views here.

def shop(request):
    products = Product.objects.all()
    return render(request, 'shop/shop.html', {'products':products})