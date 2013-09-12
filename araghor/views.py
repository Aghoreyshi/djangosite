from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'araghor/home.html')

def greyhome(request):
    return render(request, 'araghor/greyhome.html')

def cv(request):
    with open('araghor/static/arash_cv.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=arash_cv.pdf'
        return response
    pdf.closed
