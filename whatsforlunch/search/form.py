from django import forms


class SearchForm(forms.Form):

    # ll=latitude,longitude,accuracy,altitude,altitude_accuracy
    # make these hidden inputs and fill them using parameters from a map on screen
    # or make them all update in front of the user as the adjust the map

    # location
    latitude = forms.CharField(
        required= True,
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

    radius_filter = forms.CharField(
        required= False,
    )

    term = forms.CharField(
        required= False,
    )

    sort = forms.CharField(
        required= False,
    )

    category_filter = forms.CharField(
        required= False,
    )

