from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    return HttpRequest('<h1>Hello Blog</h1>')

# Create your views here.
