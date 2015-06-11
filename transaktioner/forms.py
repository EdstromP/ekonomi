from django import forms

class DatumForm(forms.Form):
    datum = forms.DateField(label='Startdatum')

