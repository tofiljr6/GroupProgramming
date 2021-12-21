from django import forms

# Create your models here.
class UploadFileForm(forms.Form):
    id = forms.CharField(max_length=40)
    file = forms.FileField()