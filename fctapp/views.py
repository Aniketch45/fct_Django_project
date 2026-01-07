from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello Welcome to Django...!</h1>")

def next(request):
    return HttpResponse("<h2>You have Visited next view</h2>")

def about(request):
    return HttpResponse("<h1>You Visited about page</h1>")
    