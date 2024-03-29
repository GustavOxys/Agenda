from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from contact.models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
            )


def create(request):
    

    context = {
        'form': ContactForm()

    }
    return render(
        request,
        'contact/create.html',
        context
    )