# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
   return render(request, 'Poke/index.html')


def dash(request):
    # user = User.

    context = {
        'Users' : User.objects.all()
        }
    return render(request, 'Poke/dashboard.html', context)



def create(request):
    User.objects.create(
        name = request.POST['name'],
        alias = request.POST['alias'],
        email = request.POST['email'],
    )
    

    return redirect ('/pokes')