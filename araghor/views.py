from django.shortcuts import render
from django.http import HttpResponseRedirect


def home(request):
    return render(request, 'araghor/home.html')

def grey(request):
    if request.session.get('grey') is None:
        request.session['grey'] = True
    request.session['grey'] = not request.session['grey']
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def cv(request):
    return render(request, 'araghor/cv.html')
