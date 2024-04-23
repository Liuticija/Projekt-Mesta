from django import forms

class CityForm(forms.Form):
    nazev = forms.CharField(max_length=30, label="Napiš název města:", required=True)
    kraj = forms.CharField(max_length=50)
    rozloha = forms.IntegerField(required=False)
    pocet = forms.IntegerField(label="Počet")