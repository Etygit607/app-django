from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class Register(View):
    
    def get(self, request):
        form = UserCreationForm()
        return render(request, "register/register.html", {"form" : form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else :
            for message in form.error_messages:
                messages.error(request, form.error_messages)
            
            return render(request, "register/register.html", {"form": form})

def sign_out(request):
    logout(request)
    return redirect('home')