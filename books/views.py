from django.shortcuts import render
from .models import *
from .forms import UserCreationForm

# Create your views here.
def book(request):
    return render(request, 'index.html')

def list(request):
    data= Book.objects.all()    
    return render(request, 'list.html', {'data':data})

def syllabus(request):
    return render(request, 'syllabus.html')

def registration(request):

    form = UserCreationForm()
    print(form)

    context = {
        'form': form
    }
    return render(request, 'register.html', context)