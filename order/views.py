from django.core.exceptions import DisallowedHost
from django.shortcuts import render
from django.http import HttpResponse
from .forms import OrderForm
from login.models import Menu
def order(request):
    submitbutton= request.POST.get("submit")

    array =[]
    dish_id = -1
    dish = None
    form= OrderForm(request.POST or None)
    if form.is_valid():
        dish_id = form.cleaned_data.get("dish_id")

        array.append (Menu.objects.get(pk=dish_id))

    context= {'form': form, 'array': array,
              'submitbutton': submitbutton}
        
    return render(request, 'waiter/order.html', context)


