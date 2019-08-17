from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def create(request):
    return render(request, 'create.html')


def event(request):
    return render(request, 'event.html')


def visitor(request):
    return render(request, 'visitor.html')
