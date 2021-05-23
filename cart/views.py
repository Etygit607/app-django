from django.shortcuts import render, redirect
from .cart import Cart
from shop.models import Product

# Create your views here.

def add_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id = product_id)
    cart.add(product = product)
    return redirect('shop')

def delete_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id = product_id)
    cart.delete(product = product)
    return redirect('shop')

def delete_one_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id = product_id)
    cart.delete_one(product = product)
    return redirect('shop')

def empty_cart(request):
    cart = Cart(request)
    cart.clean_cart()
    return redirect('shop')