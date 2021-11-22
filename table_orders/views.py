from django.shortcuts import redirect, render
from django.http import HttpResponse
from login.models import CustomUser, Table_Order, Order, Menu
from order.forms import TableForm, OrderForm
from table_orders.forms import CreateNewTableOrder, SelectTableOrderForm
from tables_layout.models import Table
# Create your views here.


def table_orders(request):
    tables = Table.objects.all
    tablesOrders = Table_Order.objects.all
    selectTableOrder = SelectTableOrderForm(request.POST or None)
    createNewTableOrder = CreateNewTableOrder(request.POST or None)
    request.session.flush()


   
   
    return render(request, 'table_orders/active_table_orders.html', {'tables': tables, 'table_orders': tablesOrders, 'createNewTableOrder':createNewTableOrder,  'selectTableOrder':selectTableOrder})

# def order_more(request):
#     print("XD")
#     table_order_id = request.session['table_order_id']
#     orderForm= OrderForm(request.POST or None)
#     return render(request, 'waiter/order.html', {'table_order_id': table_order_id, 'orderForm' : orderForm})


def pay(request):
    print("XDDDDDDDDD")

def create_table_order(request):

 
    createNewTableOrder = CreateNewTableOrder(request.POST or None)
    if(request.method == 'POST'and createNewTableOrder.is_valid()):
        table_id = createNewTableOrder.cleaned_data.get("table_id")
        table = Table.objects.get(pk = table_id)
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
        
        print(dishes)
        tableForm = TableForm(request.POST or None)
        return render(request, 'table_orders/table_order_details.html', {'table_order_id': tableOrder.id, 'tableForm': tableForm, 'dishes': dishes})