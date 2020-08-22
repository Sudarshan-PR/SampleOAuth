from django.shortcuts import render
from django.http import HttpResponse
import os

def home(request):
    return render(request, 'home/index.html')

def social(request):
    return render(request, 'home/index.html')