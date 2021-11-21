from django.shortcuts import render

# Create your views here.

def homemanagment(request):
    return render(request, 'manager/management.html')

def teammanagment(request):
    return render(request, 'manager/team.html')