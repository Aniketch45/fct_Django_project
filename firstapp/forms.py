from django import forms

class studentform(forms.Form):
    sname = forms.CharField()
    semail = forms.EmailField()

