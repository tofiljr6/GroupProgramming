from django.contrib import admin

# Register your models here.
from .models import CustomUser, Menu, Table_Order


# admin.site.register(CustomUser)
admin.site.register(Menu)
# admin.site.register(Table_Order)