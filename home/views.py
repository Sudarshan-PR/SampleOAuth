from django.shortcuts import render
from django.http import HttpResponse
import os

def home(request):
    return HttpResponse(os.environ["SAMPLE_VAR"])