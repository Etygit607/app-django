from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data = request.POST)
        if contact_form.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            content = request.POST.get("content")

            email = EmailMessage(
                "Message from App Store",
                "El usuario {} con la direccion {} te envio el siguiente mail: \n\n {}".format(name, email, content),
                "",
                ["etyvaldirmc@gmail.com"],
                reply_to = [email]
            )
            try:
                email.send()
                return redirect("/contact/?ok")
            except:
                return redirect("/contact/?failed")

    return render(request, 'contact/contact.html', {'contact_form':contact_form })