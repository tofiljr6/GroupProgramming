from django.contrib import admin

# Register your models here.
from .models import Menu, CustomUser

admin.site.register(Menu)
admin.site.register(CustomUser)
