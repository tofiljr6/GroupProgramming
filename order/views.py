from django.core.exceptions import DisallowedHost
from django.shortcuts import render
from django.http import HttpResponse
from .forms import OrderForm, TableForm
from login.models import Menu



def order(request):
    submitbutton= request.POST.get("submit")
    
    dish_id = -1
    
    orderForm= OrderForm(request.POST or None)
    tableForm = TableForm(request.POST or None)

    if orderForm.is_valid() and tableForm.is_valid():
        dish_id = orderForm.cleaned_data.get("dish_id")

       
        # //request.session.flush()
        if not 'orders' in request.session or not request.session['orders']:
            request.session['orders'] = [dish_id]
            
        else:
            orders = request.session['orders']
            orders.append(dish_id)
            request.session['orders'] = orders
                  
    order= request.session['orders']
    dishes = [] 
    for dish_id in order:
        dishes.append(Menu.objects.get(pk=dish_id))
    
    context= {'orderForm': orderForm, 'tableForm':tableForm,'dishes': dishes,
              'submitbutton': submitbutton}
        
    return render(request, 'waiter/order.html', context)


def saveOrder(request):
    dishes = request.session['orders']
    for d in dishes:
        dish = ()