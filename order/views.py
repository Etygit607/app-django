from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
#from django.core.mail import send_mail
from cart.cart import Cart
#from flask import redirect
from order.models import Order, OrderDetail

from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

@login_required(login_url="/autentication/login")
def process_order(request):
    order = Order.objects.create(user = request.user)
    cart = Cart(request)
    order_details = list()
    for key, value in cart.cart.items():
        order_details.append(OrderDetail(
            product_id = key,
            amount = value['lot'],
            user = request.user,
            order = order
        ))

    OrderDetail.objects.bulk_create(order_details)

    send_email( 
        order = order,
        order_details = order_details,
        user_name = request.user.username,
        user_email = request.user.username
    )

    messages.success(request, "El pedido se ha creado correctamente.")
    
    return redirect("../shop")

def send_email(**kwarns):
    subject = "Gracias por su pedido"
    message = render_to_string("emails/order.html",{
        "pedido": kwarns.get("order"),
        "order_details": kwarns.get("order_details"),
        "user_name": kwarns.get("user_name")
    })
    
    text_message = strip_tags(message)
    from_email = "from@example.com"
    to_email = kwarns.get("user_email")
    
    #send_mail(subject, text_message, from_email, [to], html_message = message)
    try:
        send_mail(subject, text_message, from_email, [to_email], html_message = message, fail_silently=False)
    except BadHeaderError:
        return HttpResponse("Invalid header found.")
    return HttpResponseRedirect("../shop")