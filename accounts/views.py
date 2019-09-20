from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm



class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

#this usercreation form is responsible for showing the fo 
#hw - cbv vs fbv - read about the it
#hw2 - reverse_lazy vs redirect django
# Create your views here.
