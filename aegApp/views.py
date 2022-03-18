from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
    # if 'user_id' in request.session:
    #     del request.session['user_id']
    return render(request, "index.html")

def teams(request):

    return render(request, "teams.html")


def contact(request):

    return render(request, "contact.html")


def partners(request):

    return render(request, "partners.html")


def calendar(request):

    return render(request, "calendar.html")