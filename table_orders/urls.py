from django.urls import path

from . import views
from order import views as viewsOrder

urlpatterns = [
    path('', views.table_orders, name='table_orders'),
    path('customerView/', views.table_orders_customer, name='table_orders_customer'),
    path('order_more/', viewsOrder.order, name='order_more'),
    path('pay/', views.pay, name='pay'),
    path('change_table/', views.create_table_order, name='change_table'),
    path('table_order_detail/', views.create_table_order, name='create_table_order'),
    path('table_order_detail_customer/', views.select_table_order_customer, name='select_table_order_customer'),
    path('select_table_order/', views.select_table_order, name='select_table_order'),
]
