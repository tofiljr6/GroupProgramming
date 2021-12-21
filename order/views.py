from django.core.exceptions import DisallowedHost
from django.shortcuts import render
from django.http import HttpResponse
from .forms import OrderForm, TableForm
from login.models import Order, Table_Order
from tables_layout.models import Table
from table_orders.forms import CreateNewTableOrder, SelectTableOrderForm
from menu.models import DishType, Menu




def submitOrder(request):
  

    dishes = request.session['orders']
    for d in dishes:
     
        tableOrderId = request.session['table_order_id']
        table_order = Table_Order.objects.get(pk =tableOrderId )
        dish = Menu.objects.get(id = d)
        print(dish)
        print(type(table_order))
        madeOrder = Order.objects.create(table_order_id=table_order, dish_id =dish)

        madeOrder.save()

    selectTableOrder = SelectTableOrderForm(request.POST or None)
    createNewTableOrder = CreateNewTableOrder(request.POST or None)
    tables = Table.objects.all
    tablesOrders = Table_Order.objects.all().filter(is_paid = False)
    request.session.flush()
    return render(request, 'table_orders/active_table_orders.html', {'tables': tables, 'table_orders': tablesOrders, 'createNewTableOrder':createNewTableOrder,  'selectTableOrder':selectTableOrder})



def order(request):

   
    dish_id = None
    # zmiena zawierająca id dan w biezacym zamowieniu
    order = []

    if 'Add' in request.POST:
        dish_id = int( request.POST.get('Add'))
        
        if not 'orders' in request.session or not request.session['orders']:
            request.session['orders'] = [dish_id]
           
        else:
           
            orders = request.session['orders']
            orders.append(dish_id)
            request.session['orders'] = orders

    elif 'delete' in request.POST:
        dish_id = int( request.POST.get('delete'))
        
    
           
        orders = request.session['orders']
        orders.remove(dish_id)
        request.session['orders'] = orders



    if 'orders' in request.session:
        order= request.session['orders']
    dishes = [] 

    for dish_id in order:   
        dishes.append(Menu.objects.get(pk=dish_id))
   
    type_list = DishType.objects.all()

    context= { 'dishes': dishes, 'type_list': type_list}
            
    return render(request, 'orders/order.html', context)


