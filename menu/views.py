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
    t = DishType.objects.get(id=request.POST['type'])
    t.menu_set.create(id=Menu.objects.count() + 1,
                      dish_name=request.POST['newDish'],
                      price=request.POST['newPrice'])
    return redirect("menu:index")


def removeDish(request):
    index = Menu.objects.get(id=request.POST['dishToRemove']).getId() + 1
    count = Menu.objects.count() + 1
    Menu.objects.get(id=request.POST['dishToRemove']).delete()
    for i in range(index, count):
        t = Menu.objects.get(id=i)
        t.id = i - 1
        t.save()

    return redirect("menu:index")


def addType(request):
    DishType(id=DishType.objects.count() + 1, type_name=request.POST['newType']).save()
    return redirect("menu:index")


def removeType(request):
    index = DishType.objects.get(id=request.POST['typeToRemove']).getId() + 1
    count = DishType.objects.count() + 1
    for dish in DishType.objects.get(id=request.POST['typeToRemove']).menu_set.all():
        dishIndex = dish.getId() + 1
        dishCount = Menu.objects.count() + 1
        dish.delete()
        for j in range(dishIndex, dishCount):
            t = Menu.objects.get(id=j)
            t.id = j - 1
            t.save()

    DishType.objects.get(id=request.POST['typeToRemove']).delete()
    for i in range(index, count):
        t = DishType.objects.get(id=i)
        t.id = i - 1
        t.save()

    return redirect("menu:index")


def modify(request):
    if not request.session.get('modify'):
        request.session['modify'] = True
    else:
        request.session['modify'] = None
    return redirect("menu:index")
