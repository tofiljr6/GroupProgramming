from django.shortcuts import redirect
from django.views import generic

from menu.models import Menu, DishType


class IndexView(generic.ListView):
    template_name = 'menu/index.html'
    context_object_name = 'type_list'

    def get_queryset(self):
        return DishType.objects.all()


class DetailView(generic.DetailView):
    model = Menu
    template_name = 'menu/detail.html'


def addDish(request):
    return redirect("menu:index")


def addType(request):
    return redirect("menu:index")


def modify(request):
    if not request.session.get('modify'):
        request.session['modify'] = True
    else:
        request.session['modify'] = None
    return redirect("menu:index")
