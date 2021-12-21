from django.shortcuts import redirect, render
from django.http import HttpResponse
from login.models import CustomUser, Table_Order, Order
from menu.models import Menu
from order.forms import TableForm, OrderForm
from table_orders.forms import CreateNewTableOrder, SelectTableOrderForm
from tables_layout.models import Table
# Create your views here.


def table_orders(request):
    tables = Table.objects.all
    tablesOrders = Table_Order.objects.all().filter(is_paid = False)
    selectTableOrder = SelectTableOrderForm(request.POST or None)
    createNewTableOrder = CreateNewTableOrder(request.POST or None)
    request.session.flush()


   
   
    return render(request, 'table_orders/active_table_orders.html', {'tables': tables, 'table_orders': tablesOrders, 'createNewTableOrder':createNewTableOrder,  'selectTableOrder':selectTableOrder})


def table_orders_customer(request):
    # TO-DO
    userId = 1
    tables = Table.objects.all
    tablesOrders = Table_Order.objects.all().filter(user_id =userId)
    selectTableOrder = SelectTableOrderForm(request.POST or None)
    createNewTableOrder = CreateNewTableOrder(request.POST or None)
    request.session.flush()

    return render(request, 'table_orders/active_table_orders.html', {'tables': tables, 'table_orders': tablesOrders, 'createNewTableOrder':createNewTableOrder,  'selectTableOrder':selectTableOrder})
def pay(request):
    table_order_idx = request.session['table_order_id']
    tableOrder = Table_Order.objects.get(pk = table_order_idx)
    tableOrder.is_paid = True
    tableOrder.save()

    table_id = tableOrder.table_id.pk
    
    table = Table.objects.get(pk = table_id)
    table.state = "FREE"
    table.save()

    points = 0

    orders = Order.objects.all().filter(table_order_id = table_order_idx)
    
    for order in orders:
        dish_idx = order.dish_id.pk
        dish = Menu.objects.get(pk = dish_idx)
        points = points + dish.price


    
    user_id =  tableOrder.user_id.pk
    user = CustomUser.objects.get(pk =user_id)
    user.point_number = user.point_number + points
    print(points)
    user.save()
    return table_orders(request)

def create_table_order(request):

 
    createNewTableOrder = CreateNewTableOrder(request.POST or None)
    if(request.method == 'POST'and createNewTableOrder.is_valid()):
        table_id = createNewTableOrder.cleaned_data.get("table_id")
        print(table_id)
        table = Table.objects.get(pk = table_id)
        table.state = "BUSY"
       
        table.save()
        # do poprawy!!! uzupelnij o waiterid i userid
        user = CustomUser.objects.get(pk=1)

        tableOrder = Table_Order(table_id= table,user_id = user,waiter_id = user, is_paid =False)
        tableOrder.save()
        tableForm = TableForm(request.POST or None)
        request.session['table_order_id'] = tableOrder.id
        
        return render(request, 'table_orders/table_order_details.html', {'table_order_id': tableOrder.id, 'tableForm': tableForm})





def select_table_order(request):

 
    selectTableOrderForm = SelectTableOrderForm(request.POST or None)
    
    if(request.method == 'POST' and selectTableOrderForm.is_valid()):
        table_order_idx = selectTableOrderForm.cleaned_data.get("table_order_id")
        tableOrder = Table_Order.objects.get(pk = table_order_idx)
        
        orders = Order.objects.filter(table_order_id = tableOrder)
        dishes = []
        
        for o in orders:
            print(o.dish_id)
            dishes.append(o.dish_id)
        request.session['table_order_id'] = tableOrder.id
        
        
        tableForm = TableForm(request.POST or None)
        return render(request, 'table_orders/table_order_details.html', {'table_order_id': tableOrder.id, 'tableForm': tableForm, 'dishes': dishes})


def select_table_order_customer(request):

 
    selectTableOrderForm = SelectTableOrderForm(request.POST or None)
    
    if(request.method == 'POST' and selectTableOrderForm.is_valid()):
        table_order_idx = selectTableOrderForm.cleaned_data.get("table_order_id")
        tableOrder = Table_Order.objects.get(pk = table_order_idx)
        
        orders = Order.objects.filter(table_order_id = tableOrder)
        dishes = []
        
        for o in orders:
            dishes.append(o.dish_id)
        request.session['table_order_id'] = tableOrder.id
        
       
        tableForm = TableForm(request.POST or None)
        return render(request, 'table_orders/table_order_details.html', {'table_order_id': tableOrder.id, 'tableForm': tableForm, 'dishes': dishes})