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


def modify(request):
    if not request.session.get('modify'):
        request.session['modify'] = True
    else:
        c = 1
        while True:
            if request.POST.get(f'newTypeName{c}') is not None:
                if request.POST.get(f'newTypeName{c}', '') != '':
                    d = DishType.objects.get(id=c)
                    d.type_name = request.POST[f'newTypeName{c}']
                    d.save()
            elif request.POST.get(f'addedNewTypeName{c}') is not None:
                if request.POST.get(f'addedNewTypeName{c}', '') != '':
                    DishType(id=DishType.objects.count() + 1, type_name=request.POST[f'addedNewTypeName{c}']).save()
            else:
                break
            c += 1
        request.session['modify'] = None
    return redirect("menu:index")


# def addDish(request):
#     t = DishType.objects.get(id=request.POST['type'])
#     t.menu_set.create(id=Menu.objects.count() + 1,
#                       dish_name=request.POST['newDish'],
#                       price=request.POST['newPrice'])
#     return redirect("menu:index")
#
#
# def deleteObjects(index, count, table):
#     for i in range(index, count):
#         t = table.objects.get(id=i)
#         t.id = i - 1
#         t.save()
#
#     if index != count:
#         table.objects.get(id=count-1).delete()
#
#
# def removeDish(request):
#     index = Menu.objects.get(id=request.POST['dishToRemove']).getId() + 1
#     count = Menu.objects.count() + 1
#     Menu.objects.get(id=request.POST['dishToRemove']).delete()
#     deleteObjects(index, count, Menu)
#
#     return redirect("menu:index")
#
#
# def editDish(request):
#     d = Menu.objects.get(id=request.POST['id'])
#     d.dish_name = request.POST['newName']
#     if request.POST['newPrice'] != "":
#         d.price = request.POST['newPrice']
#     d.save()
#
#     return redirect("menu:index")
#
#
# def addType(request):
#     DishType(id=DishType.objects.count() + 1, type_name=request.POST['newType']).save()
#     return redirect("menu:index")
#
#
# def removeType(request):
#     index = DishType.objects.get(id=request.POST['typeToRemove']).getId() + 1
#     count = DishType.objects.count() + 1
#     for dish in DishType.objects.get(id=request.POST['typeToRemove']).menu_set.all():
#         dishIndex = dish.getId() + 1
#         dishCount = Menu.objects.count() + 1
#         dish.delete()
#         deleteObjects(dishIndex, dishCount, Menu)
#
#     DishType.objects.get(id=request.POST['typeToRemove']).delete()
#     deleteObjects(index, count, DishType)
#
#     return redirect("menu:index")
#
#
# def editType(request):
#     d = DishType.objects.get(id=request.POST['id'])
#     d.type_name = request.POST['newName']
#     d.save()
#
#     return redirect("menu:index")
