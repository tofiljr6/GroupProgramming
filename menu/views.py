from django.shortcuts import redirect
from django.views import generic

from menu.models import Menu, DishType
from login.models import CustomUser

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
        Menu.objects.all().delete()
        DishType.objects.all().delete()
        c = 1
        k = 1
        while True:
            if request.POST.get(f'newTypeName{c}') is not None:
                if request.POST.get(f'newTypeName{c}', '') != '':
                    d = DishType(id=DishType.objects.count() + 1,
                                 type_name=request.POST[f'newTypeName{c}'])
                    d.save()

                    while True:
                        if request.POST.get(f'{c}newDishName{k}') is not None:
                            if request.POST.get(f'{c}newDishName{k}', '') != '' and \
                                    request.POST.get(f'{c}newDishPrice{k}', '') != '':
                                d.menu_set.create(id=Menu.objects.count() + 1,
                                                  dish_name=request.POST[f'{c}newDishName{k}'],
                                                  price=request.POST[f'{c}newDishPrice{k}'])
                        else:
                            break
                        k += 1
            else:
                break
            c += 1

        request.session['modify'] = None
    return redirect("menu:index")


def cancel(request):
    request.session['modify'] = False
    return redirect("menu:index")
