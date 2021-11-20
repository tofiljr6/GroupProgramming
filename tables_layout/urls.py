from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.add, name='add'),
    path('remove/', views.remove, name='remove'),
]
