from django import forms


class MyForm(forms.Form):
    language = forms.CharField(max_length=255)