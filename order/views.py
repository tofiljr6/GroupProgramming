from django.core.exceptions import DisallowedHost
from django.shortcuts import render
from django.http import HttpResponse
from .forms import OrderForm, TableForm
from login.models import Menu,Order, Table_Order
from tables_layout.models import Table
from table_orders.forms import CreateNewTableOrder, SelectTableOrderForm

def order(request):

    submitbutton= request.POST.get("submit")
    dish_id = None
    # zmiena zawierająca id dan w biezacym zamowieniu
    order = []
    orderForm= OrderForm(request.POST or None)
    
    if orderForm.is_valid():
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

   
    context= {'orderForm': orderForm, 'dishes': dishes,
                'submitbutton': submitbutton}
            
    return render(request, 'waiter/order.html', context)

def submitOrder(request):
    dishes = request.session['orders']
    for d in dishes:

        
        tableOrderId = request.session['table_order_id']
        table_order = Table_Order.objects.get(pk =tableOrderId )
        dish = Menu.objects.get(pk = d)


        order = Order(table_order_id=table_order, dish_id =dish)
        order.save()

    selectTableOrder = SelectTableOrderForm(request.POST or None)
    createNewTableOrder = CreateNewTableOrder(request.POST or None)
    tables = Table.objects.all
    tablesOrders = Table_Order.objects.all
    request.session.flush()
    return render(request, 'table_orders/active_table_orders.html', {'tables': tables, 'table_orders': tablesOrders, 'createNewTableOrder':createNewTableOrder,  'selectTableOrder':selectTableOrder})