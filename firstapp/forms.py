from django import forms

class studentform(forms.Form):
    sname = forms.CharField()
    semail = forms.EmailField()

class student(forms.Form):
    sno = forms.IntegerField()
    name = forms.CharField()
    sfees = forms.DecimalField()
    