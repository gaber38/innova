from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView


from .models import *
from .forms import *


class ContactAdd(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = "create_contact.html"
    success_url = reverse_lazy("contact_list")
    context_object_name = "contact"


    def form_valid(self, form):
        response = super().form_valid(form)

        phone_numbers = form.cleaned_data['phone_numbers']
        for number in phone_numbers:
            Phonenumber.objects.create(contact=self.object, number=number)

        return response


class ContactList(ListView):
    model = Contact
    template_name = "list_contact.html"
    context_object_name = "contacts"
    paginate_by = 10


class ContactDetails(DetailView):
    model = Contact
    template_name = "details_contact.html"
    context_object_name = "contact"