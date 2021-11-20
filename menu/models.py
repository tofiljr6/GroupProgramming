from django.db import models


class DishType(models.Model):
    type_name = models.CharField(max_length=200)

    def __str__(self):
        return self.type_name


class Menu(models.Model):
    type = models.ForeignKey(DishType, on_delete=models.CASCADE)  # TODO
    dish_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.dish_name
