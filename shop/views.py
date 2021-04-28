from django.shortcuts import render, HttpResponse

# Create your views here.

def shop(request):
    return render(request, 'shop/shop.html')