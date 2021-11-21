from django.db import models


class DishType(models.Model):
    id = models.IntegerField(primary_key=True)
    type_name = models.CharField(max_length=200)

    def __str__(self):
        return self.type_name

    def getId(self):
        return self.id


class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    dish_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.dish_name

    def getId(self):
        return self.id
