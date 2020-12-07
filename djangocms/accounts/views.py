from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import *
from accounts.models import User


def user_login(request):
    if request.method == "GET":
        return render(request, 'login.html', {'form': AuthenticationForm()})

    # If POST
    lf = AuthenticationForm(data=request.POST)
    if lf.is_valid():
        username = lf.cleaned_data['username']
        password = lf.cleaned_data['password']

        user = authenticate(request, username=username, password=password)
        login(request, user)
        if user.is_superuser:
            pass
        return redirect('staff_home')

    # If invalid
    return render(request, 'login.html', {'form': lf})


def register(request):
    if request.method == "GET":
        return render(request, 'register.html', {'form': RegistrationForm()})

    # If the request method is POST
    rf = RegistrationForm(request.POST)
    if rf.is_valid():
        user=User()
        user.name = rf.cleaned_data['name']
        user.email = rf.cleaned_data['email']
        user.set_password(rf.cleaned_data['password'])
        user.save()
        # Saving the user to database
        return redirect('login')

    # If the form is invalid
    return render(request, 'register.html', {'form': rf})


def staff_logout(request):
    logout(request)
    return redirect('home')
