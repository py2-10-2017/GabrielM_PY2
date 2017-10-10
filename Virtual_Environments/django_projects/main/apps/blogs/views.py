# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    response = "Placeholder to later display a list of all the blogs"
    return HttpResponse(response)

def new(request):
    response = "Placeholder to display a new form to create a new blog post"
    return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request, blog_id):
    print blog_id
    return HttpResponse("Placeholder to display blog{}".format(blog_id))

def edit(request, blog_id):
    return HttpResponse("placeholder to edit blog {}".format(blog_id))

def destroy(request, blog_id):
    return redirect('/')