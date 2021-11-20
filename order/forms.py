from django import forms

class OrderForm(forms.Form):
    dish_id = forms.IntegerField()

