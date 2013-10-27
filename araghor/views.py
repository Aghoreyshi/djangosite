from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'araghor/home.html')

def greyhome(request):
    return render(request, 'araghor/greyhome.html')

def cv(request):
    return render(request, 'araghor/cv.html')
