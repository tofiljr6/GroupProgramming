from django.contrib import admin

# Register your models here.
from .models import CustomUser, Order, Table_Order
from tables_layout.models import Table
from menu.models import Menu
admin.site.register(Menu)
admin.site.register(CustomUser)
admin.site.register(Table_Order)
admin.site.register(Table)
admin.site.register(Order)