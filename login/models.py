from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.fields import DateField
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    name = models.CharField(max_length=200, default="")
    surname = models.CharField(max_length=200, default="")
    # email = models.CharField(max_length=200)
    point_number =models.IntegerField(default=0)
    role = models.TextChoices('Role', 'GUEST WAITER KITCHEN BAR MANAGER')

class Table(models.Model):
    isFree = models.TextChoices('isFree', 'FREE TAKEN RESERVED')

class Table_Order(models.Model):
    table_id = models.ForeignKey(Table, on_delete= models.SET_NULL, null= True)
    user_id = models.ForeignKey(CustomUser, on_delete= models.SET_NULL, null= True, related_name='user')
    waiter_id = models.ForeignKey(CustomUser, on_delete= models.SET_NULL, null= True, related_name='waiter')
    is_paid = models.BooleanField(default= False)

class Supply(models.Model):
    product = models.CharField(max_length=200)
    amount = models.FloatField()
    date = models.DateField()
    realised = models.BooleanField(default=False)



class Menu(models.Model):
    type = models.TextChoices('Type', 'DRINK DISH')
    name = models.CharField(max_length=200)
    price = models.FloatField()

class Order(models.Model):
    table_order_id = models.ForeignKey(Table_Order, on_delete= models.SET_NULL, null= True)
    dish_id = models.ForeignKey(Menu, on_delete=SET_NULL, null= True)
    where = models.TextChoices('Where', 'BAR KITCHEN')


class History(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete= models.SET_NULL, null= True)
    order_id = models.ForeignKey(Order, on_delete= models.SET_NULL, null= True)



    
