from django import forms
from whatsforlunch.search.connect import api_request


class SearchForm(forms.Form):

    # ll=latitude,longitude,accuracy,altitude,altitude_accuracy
    # make these hidden inputs and fill them using parameters from a map on screen
    # or make them all update in front of the user as the adjust the map

    # location
    location = forms.CharField(
        required= False
    )

    latitude = forms.CharField(
        required= False,
    )

    longitude = forms.CharField(
        required= False,
    )

    accuracy = forms.CharField(
        required= False,
    )

    altitude = forms.CharField(
        required= False,
    )

    altitude_accuracy = forms.CharField(
        required= False,
    )

    radius = forms.CharField(
        required= False,
    )

    term = forms.CharField(
        required= False,
    )

    sort = forms.CharField(
        required= False,
    )

    category = forms.CharField(
        required= False,
    )

    def search(self):
        # i want this to allow me to search by just location too?
        # or always require full lat/long...
        url_params = {
            'latitude': self.clean['latitude'],
            'longitude': self.clean['longitude'],
            'accuracy': self.clean['accuracy'],
            'altitude': self.clean['altitude'],
            'altitude_accuracy': self.clean['altitude_accuracy'],
            'radius_filter': self.clean['radius'],
            'term': self.clean['term'],
            'sort': self.clean['sort'],
            'category_filter': self.clean['category']
        }
        return api_request(url_params)