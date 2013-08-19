from django.shortcuts import render


def home(request):
    return render(request, 'araghor/home.html')

def greyhome(request):
    return render(request, 'araghor/greyhome.html')
