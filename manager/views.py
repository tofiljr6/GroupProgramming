from django.shortcuts import render
from django.views import generic

from login.models import CustomUser

class IndexView(generic.ListView):
    template_name = 'manager/team.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        return CustomUser.objects.all()


def homemanagment(request):
    return render(request, 'manager/management.html')


def teammanagment(request):
    return render(request, 'manager/team.html')
