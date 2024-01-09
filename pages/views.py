from django.shortcuts import render
from django.core.mail import send_mail
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render

def home(request):
    return render(request, "pages/home.html", {})
