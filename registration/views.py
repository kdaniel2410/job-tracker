from django.views import generic
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm


class RegisterView(generic.CreateView):
    template_name = "registration/register.html"
    form_class = UserCreationForm
    success_url = "/"
