from django import forms

class OrderForm(forms.Form):
    dish_id = forms.IntegerField()

class TableForm(forms.Form):
    table_id = forms.IntegerField()