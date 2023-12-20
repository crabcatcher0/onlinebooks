from django.shortcuts import render
from .models import *

# Create your views here.
def book(request):
    return render(request, 'index.html')

def list(request):
    data= Book.objects.all()    
    return render(request, 'list.html', {'data':data})