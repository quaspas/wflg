from django import forms
from whatsforlunch.place.models import Place


class PlaceSaveForm(forms.ModelForm):

    api_id= forms.CharField()

    class Meta:
        model = Place
        fields = ['api_id ']
