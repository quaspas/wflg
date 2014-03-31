from django import forms
from whatsforlunch.search.connect import api_request


class SearchSimpleForm(forms.Form):

    # ll=latitude,longitude,accuracy,altitude,altitude_accuracy
    # make these hidden inputs and fill them using parameters from a map on screen
    # or make them all update in front of the user as the adjust the map

    # location
    location = forms.CharField(widget=forms.TextInput(attrs={
        'name': 'location',
        'placeholder': 'location',
    }))

    term = forms.CharField(widget=forms.TextInput(attrs={
        'name': 'term',
        'placeholder': 'what do you feel like eating?',
    }))

    def search(self):
        url_params = {
            'location': self.cleaned_data['location'],
            'term': self.cleaned_data['term'],
        }
        return api_request(url_params)
