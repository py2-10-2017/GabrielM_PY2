# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random
import string

def random_Word(n):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))

# Create your views here.

def index(request):
    try:
        request.session['tries']
    except KeyError:
        request.session['tries'] = 0

    return render(request, "random_Word/index.html")

def generate(request):
    request.session['tries'] += 1
    request.session['word'] = random_Word(10)
    return redirect('/random_Word')
    

def reset(request):
    del request.session['tries']
    del request.session['word']
    return redirect('/random_Word')