from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# TODO proper error handling


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_verification = request.POST['password_verification']

        if password == password_verification:

            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(
                    username=username, password=password)
                auth.login(request, user)
                return redirect('dashboard')

            else:
                messages.error(request, 'Username is taken')

        else:
            messages.error(request, 'Passwords have to be equal')

    return redirect('index')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')

        else:
            messages.error(request, 'Invalid credentials')

    return redirect('index')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')

    return redirect('dashboard')
