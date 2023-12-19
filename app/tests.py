# phonebook/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Contact, PhoneNumber


class ContactModelTest(TestCase):
    def test_contact_creation(self):
        contact = Contact.objects.create(name="Eslam Gaber")
        self.assertEqual(contact.name, "Eslam Gaber")
        self.assertEqual(Contact.objects.count(), 1)

class ContactListWithNumbersViewTest(TestCase):
    def setUp(self):
        self.contact1 = Contact.objects.create(name="Eslam")
        self.phone1_contact1 = PhoneNumber.objects.create(contact=self.contact1, number="123456789")

        self.contact2 = Contact.objects.create(name="Gaber")
        self.phone1_contact2 = PhoneNumber.objects.create(contact=self.contact2, number="987654321")
        self.phone2_contact2 = PhoneNumber.objects.create(contact=self.contact2, number="111222333")

    def test_contact_list_view(self):
        url = reverse('contact_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list_contact.html')

        
        expected_data = [
            {'name': 'Eslam', 'numbers': ['123456789']},
            {'name': 'Gaber', 'numbers': ['987654321', '111222333']},
        ]
        self.assertEqual(response.context['contacts'], expected_data)

class ContactCreateViewTest(TestCase):
    def test_contact_create_view(self):
        data = {'name': 'Eslam Gaber', 'phone_numbers': '1234554577,6789011245'}
        response = self.client.post(reverse('contact_add'), data)
        self.assertEqual(response.status_code, 302) 
        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(PhoneNumber.objects.count(), 2)

