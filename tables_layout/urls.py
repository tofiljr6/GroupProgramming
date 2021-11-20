from django.urls import path

from . import views

app_name = 'tables_layout'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.add, name='add'),
    path('remove/', views.remove, name='remove'),
]
