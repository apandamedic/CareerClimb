from django.shortcuts import render
from django.http import HttpResponse

def profile(request):
    return HttpResponse('Profile Page')

def room(request):
    return HttpResponse('Room')

