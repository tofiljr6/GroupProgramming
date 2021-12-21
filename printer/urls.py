from django.urls import path
from . import views

app_name = 'printer'
urlpatterns = [
    path('printer/', views.homeprinter, name='homeprinter'),
    path('printer/print', views.printorder, name='printorder'),

]