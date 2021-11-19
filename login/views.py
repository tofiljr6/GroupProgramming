from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate

def home(request):
    return render(request, 'login/home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'login/signupuser.html', {'form':UserCreationForm()})
    else:
        # create a new user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'login/signupuser.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username.'})
        else:
            # Tell the user the password didn't match
            return render(request, 'login/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'login/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, 'login/loginuser.html', {'form':AuthenticationForm(), 'error':"Username and password did not match"})
        else:
            login(request, user)
            return redirect('currenttodos')
            
            
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
        # return HttpResponseRedirect('login/home.html')
            
            
def currenttodos(request):
    return render(request, 'login/currenttodos.html')