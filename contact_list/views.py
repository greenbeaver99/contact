from django.shortcuts import render
from .models import Contact


def index(request):
    contacts = Contact.objects.order_by('first_name')
    context = {'contacts': contacts}
    return render(request, 'index.html', context)


def contact(request, contact_id):
    contact_object = Contact.objects.get(id=contact_id)
    context = {'contact': contact_object}
    return render(request, 'contact.html', context)
