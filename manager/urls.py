from django.urls import path

from . import views

app_name = 'manager'
urlpatterns = [
    path('managment/', views.homemanagment, name='homemanagment'),
    path('teammanagment/', views.IndexView.as_view(), name="teammanagment"),
]