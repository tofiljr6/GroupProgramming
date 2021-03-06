from django.urls import path

from . import views

app_name = 'menu'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('modify/', views.modify, name='modify'),
    path('cancel/', views.cancel, name='cancel'),
]
