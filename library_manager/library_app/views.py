from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from .models import Library, Member

# Create your views here.


def login(request):
    if request.method == "POST":
        if authenticate(username=request.POST['username'], password=request.POST['password']):
            request.session['login'] = True
            request.session['username'] = request.POST['username']
            return HttpResponseRedirect('/library/')
        else:
            request.session['login'] = False
            return render(request, 'login.html', {
                'error_message': 'Incorrect Credentials'
            })
    return render(request, 'login.html')

def library(request):
    queryset = Library.objects.all()
    if request.session.get('login', True):
        return render(request, 'library.html', {
            'books': queryset,
            'borrowedBooks': getBorrowedBooks(request.session.get('username'))
        })

def getBorrowedBooks(username):
    try:
        member = Member.objects.get(member_username=username)
        if member:
            borrowedBooks = Library.objects.filter(book_holder=member)
            return borrowedBooks
    except:
        return Library.objects.none()


def member(request):
    queryset = Member.objects.all()
    if request.session.get('login', True):
        return render(request, 'member.html', { 'members': queryset })

def logout(request):
    request.session['login'] = True
    HttpResponseRedirect('/login/')