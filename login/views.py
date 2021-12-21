from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from login.models import CustomUser
from login.forms import signUpForm
from django.contrib import messages

def home(request):
    return render(request, 'login/home.html')

def startpage(request):
    return render(request, 'login/startpage.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'login/signupuser.html', {'form':signUpForm()})
    else:
        # create a new user
        form = signUpForm(request.POST)
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = CustomUser.objects.create_user(username=request.POST['username'],
                                                      password=request.POST['password1'],
                                                      email=request.POST['email'],
                                                      point_number=0,
                                                      name=request.POST['name'],
                                                      surname=request.POST['surname'],
                                                      role='GUEST')
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                messages.info(request, "The username has already benn taken.. Please choose a new username.")
                return render(request, 'login/signupuser.html', {'form':signUpForm(), 'error':'That username has already been taken. Please choose a new username.'})
        else:
            # Tell the user the password didn't match
            messages.info(request, "Passwords do not match")
            return render(request, 'login/signupuser.html', {'form':signUpForm(), 'error':'password did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'login/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        cu = CustomUser.objects.get(username=request.POST["username"]).role

        if user is None:
            messages.info(request, "Username and password did not match")
            return render(request, 'login/loginuser.html', {'form':AuthenticationForm(), 'error':"Username and password did not match"})
        else:
            # messages.info(request, cu)
            # return render(request, 'login/loginuser.html',
            #               {'form': AuthenticationForm(), 'error': "Username and password did not match"})
            login(request, user)
            if cu == 'MANAGER':
                return redirect('manager:homemanagment')
            else:
                return redirect('currenttodos')
            
            
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
        # return HttpResponseRedirect('login/home.html')
            
            
def currenttodos(request):
    return render(request, 'login/currenttodos.html')