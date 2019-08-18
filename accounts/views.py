from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def index(request):
    user = request.user

    context = {
        'user': user,
    }

    return render(request, 'index.html', context)


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_verification = request.POST['password_verification']

        if password != password_verification:
            messages.error(request, 'passwords have to be equal')
            return redirect('index')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'username is taken')
            return redirect('index')

        user = User.objects.create_user(
            username=username, password=password
        )
        auth.login(request, user)

        messages.success(request, 'registered')
        return redirect('dashboard')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'invalid credentials')
            return redirect('index')

        auth.login(request, user)

        messages.success(request, 'logged in')
        return redirect('dashboard')


def logout(request):
    if request.method == 'POST':

        auth.logout(request)

        messages.success(request, 'logged out')
        return redirect('index')
