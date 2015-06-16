from django import forms
from .models import Transaktion

#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, ButtonHolder, Submit


class DatumForm(forms.Form):
    datum = forms.DateField(label='Startdatum')


class TransaktionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TransaktionForm, self).__init__(*args, **kwargs)
        self.fields['underkategori'].required = False

    class Meta:
        model = Transaktion
        fields = [
                'reskontradatum',
                'transaktionsdatum',
                'text',
                'belopp',
                'kommentar',
                'kategori',
                'underkategori'
        ]

        widgets = {
                'reskontradatum': forms.DateInput(attrs={'class':'datepicker'}),
        }





#class TransaktionForm(forms.ModelForm):
"""
class TransaktionForm(UpdateView):
    def __init__(self, *args, **kwargs):
        super(TransaktionForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
                'reskontradatum',
                'transaktionsdatum',
                'text',
                'belopp',
                'kategori',
                ButtonHolder(
                    Submit('uppdatera', 'Uppdatera', css_class='btn-primary')
                )
        )
"""
