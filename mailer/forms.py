from django import forms


class NewsletterForm(forms.Form):
    recipient = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)


class ReceiptForm(forms.Form):
    recipient = forms.EmailField()
