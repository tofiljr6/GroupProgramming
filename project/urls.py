"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from login import views



urlpatterns = [
    path('admin/', admin.site.urls),

    path('mailer/', include('mailer.urls')),
    
    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    
    # example
    path('', views.startpage, name='startpage'),
    path('home/', views.home, name='home'),
    path('example/', views.currenttodos, name='currenttodos'),

    # menu
    path('menu/', include('menu.urls')),

    # manager
    path('managment/', include('manager.urls')),

    # tables layout
    path('tables_layout/', include('tables_layout.urls')),
    
    path('order/', include('order.urls')),

    path('table_orders/', include('table_orders.urls'))
]
