from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import urllib.request

# Create your views here.


def filter(request):
    return render(request, 'main/filter.html')


def input(request):
    return render(request, 'main/input.html')


def output(request):
    return render(request, 'main/output.html')
