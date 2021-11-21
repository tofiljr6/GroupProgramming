from django.urls import path

from . import views

app_name = 'menu'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('addDish/', views.addDish, name='addDish'),
    path('addType/', views.addType, name='addType'),
    path('removeType/', views.removeType, name='removeType'),
    path('removeDish/', views.removeDish, name='removeDish'),
    path('modify/', views.modify, name='modify'),
]
