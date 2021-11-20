from django.urls import path

from . import views

urlpatterns = [
    path('pog', views.order, name='order'),
]

