from django.db import models

class Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Phonenumber(models.Model):
    id = models.BigAutoField(primary_key=True)
    number = models.CharField(max_length=11)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.number
    

    
