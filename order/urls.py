from django.urls import path

from . import views

urlpatterns = [
    path('submitOrder/', views.submitOrder, name='submit_order'),
    path('', views.order, name='order'),
   
]

