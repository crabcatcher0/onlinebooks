from django.contrib.auth import authenticate, login as auth_login
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
            username = request.POST.get('username')
            password = request.POST.get('password')
            print("Is Form Valid?", loginform.is_valid())

            user = authenticate(request, username = username, password = password)

            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')
            else:
                 print(loginform.errors)
            

    context = {
        'loginform': loginform
    }
    return render(request, 'login.html', context)


def dashboard(request):
    return render(request, 'dashboard.html')