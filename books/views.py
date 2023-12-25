from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth

from django.shortcuts import render, redirect
from .forms import RegisterUser, LoginUser
from .models import *

# Create your views here.
def book(request):
    return render(request, 'index.html')



def list(request):
    data= Book.objects.all()    
    return render(request, 'list.html', {'data':data})



def syllabus(request):
    return render(request, 'syllabus.html')




def registration(request):

    form = RegisterUser()
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'register.html', context)



def login(request):
    loginform = LoginUser()

    if request.method == 'POST':
        loginform = LoginUser(request, data = request.POST)

        if loginform.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, email = email, password = password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')

        


    context = {
        'loginform': loginform
    }
    return render(request, 'login.html', context)


def dashboard(request):
    return render(request, 'dashboard.html')