from django import forms

class CreateNewTableOrder(forms.Form):
    table_id = forms.IntegerField()

class SelectTableOrderForm(forms.Form):
    table_order_id = forms.IntegerField()
    