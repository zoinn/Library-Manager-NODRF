from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate


# Create your views here.


def login(request):
    if request.method == "POST":
        if authenticate(username=request.POST['username'], password=request.POST['password']):
            request.session['login'] = True
            request.session['username'] = request.POST['username']
            return HttpResponseRedirect('/library/')
        else:
            request.session['login'] = False
            return HttpResponse("Incorrect Credentials: 401")
    return render(request, 'login.html')


def library(request):
    if request.session.get('login', True):
        return render(request, 'library.html')


def member(request):
    if request.session.get('login', True):
        return render(request, 'member.html')

def logout(request):
    request.session['login'] = True
    HttpResponseRedirect('/login/')