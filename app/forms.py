from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    phone_numbers = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'separated by commas'}), required=True)
    
    class Meta:
        model = Contact
        fields = ["name"]

    def clean_phone_numbers(self):
        data = self.cleaned_data['phone_numbers']
        numbers = [number.strip() for number in data.split(',') if number.strip()]
        print("*********", numbers)
        return numbers





