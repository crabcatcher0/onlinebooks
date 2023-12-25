from django.urls import path
from .views import *

urlpatterns = [
     path('', book, name = "book"),
    path('list/', list, name="list"),
    path('syllabus/', syllabus, name="syllabus"),
    path('register/', registration, name="register"),
    path('login/', login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
]