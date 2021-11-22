from django.urls import path

from . import views
from order import views as viewsOrder

urlpatterns = [
    path('', views.table_orders, name='table_orders'),
    path('order_more/', viewsOrder.order, name='order_more'),
    path('pay/', views.pay, name='pay'),
    path('change_table/', views.create_table_order, name='change_table'),
    path('table_order_detail/', views.create_table_order, name='create_table_order'),
    path('select_table_order/', views.select_table_order, name='select_table_order'),
]
