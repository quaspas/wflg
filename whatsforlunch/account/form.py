from django.contrib.auth import authenticate
from django.utils.translation import ugettext as _
from django import forms


class AccountLoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'required': 'required',
        'placeholder': _('Username'),
        'class': 'form-control',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'required': 'required',
        'placeholder': _('Password'),
        'class': 'form-control',
    }))

    error_messages = {
        'invalid_login': _('Please ensure you entered the correct email and password.'),
        'inactive': _('Your account has been deactivated. Please contact an administrator to be reactivated.'),
    }

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super(AccountLoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(self.error_messages['invalid_login'])
            elif not self.user_cache.is_active:
                raise forms.ValidationError(self.error_messages['inactive'])

        return self.cleaned_data

    def get_user(self):
        return self.user_cache
