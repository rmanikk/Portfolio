from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactMessageForm


def contact(request):

    if request.method == "POST":

        form = ContactMessageForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Your message has been sent successfully."
            )

            return redirect("contact:contact")

    else:

        form = ContactMessageForm()

    return render(
        request,
        "contact/contact.html",
        {
            "form": form,
        },
    )