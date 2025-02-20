from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def setsession(request):
    request.session['username'] = 'hello'
    request.session.set_expiry(30)
    return HttpResponse("Session is set.")

def getsession(request):
    request.session.g
