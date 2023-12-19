from django.urls import path
from .views import *

urlpatterns = [
    path("list", ContactList.as_view(), name="contact_list"),
    path("create", ContactAdd.as_view(), name="contact_add"),
    path("<int:pk>", ContactDetails.as_view(), name="contact_details"),
]
