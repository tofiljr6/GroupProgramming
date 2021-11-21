from django.urls import path

from . import views

app_name = 'manager'
urlpatterns = [
    path('managment/', views.homemanagment, name='homemanagment'),
    path('teammanagment/', views.teammanagment, name="teammanagment")
]