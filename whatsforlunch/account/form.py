from PIL import Image
from django import forms
from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.forms.widgets import ClearableFileInput, EmailInput
from django.template import loader
from django.utils.http import int_to_base36
from django.utils.translation import ugettext as _
from whatsforlunch.account.models import User
from whatsforlunch.core.fields import EmailField
from whatsforlunch.settings import SITE_DOMAIN, SITE_PROTOCOL


class AccountLoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'required': 'required',
        'placeholder': _('Username'),
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'required': 'required',
        'placeholder': _('Password'),
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


class AccountCreateForm(forms.Form):

    email = forms.EmailField(widget=forms.TextInput(attrs={
        'required': 'required',
        'placeholder': _('Email'),
    }))

    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': _('Username'),
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'required': 'required',
        'placeholder': _('Password'),
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'required': 'required',
        'placeholder': _('Password'),
    }))


class SendPasswordResetEmail(object):

    def send_email(self):
        context = {
            'domain': SITE_DOMAIN,
            'protocol': SITE_PROTOCOL,
            'uid': int_to_base36(self.user.pk),
            'token': PasswordResetTokenGenerator().make_token(self.user)
        }
        send_mail(
            subject=_('Password Reset'),
            message=loader.render_to_string('account/emails/account-password-reset-email.txt', context),
            from_email=DEFAULT_FROM_EMAIL,
            recipient_list=[self.user.email],
        )

class AccountPasswordResetForm(forms.Form, SendPasswordResetEmail):

    email = EmailField(widget=EmailInput(attrs={
        'required': 'required',
        'placeholder': _('Email'),
        'class': 'form-control',
    }))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            self.user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise forms.ValidationError(_('There is no account that matches the email entered.'))
        return email


class AccountPasswordSetForm(forms.Form):

    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(attrs={
            'required': 'required',
            'placeholder': _('Password'),
            'class': 'form-control',
        }),
    )

    password2 = forms.CharField(
        label=_('Confirm Password'),
        widget=forms.PasswordInput(attrs={
            'required': 'required',
            'placeholder': _('Confirm Password'),
            'class': 'form-control',
        }),
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(AccountPasswordSetForm, self).__init__(*args, **kwargs)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_('The passwords entered did not match.'))
        return password2

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data['password1'])
        if commit:
            self.user.save()
        return self.user


class AccountSettingsUpdateForm(forms.ModelForm):

    full_name = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )

    avatar = forms.FileField(
        required=False,
        widget=ClearableFileInput(attrs={
            'id':'file'
        })
    )

    def clean_avatar(self):
        # size in bytes, 1mb = 1048576 bytes, 10mb limit
        MAX_IMAGE_FILE_SIZE = 1048576*10
        SUPPORTED_IMAGE_FORMATS = ['JPG','JPEG','PNG']

        file = self.cleaned_data.get('avatar')

        if file:
            if file.size > MAX_IMAGE_FILE_SIZE:
               raise forms.ValidationError(_('{} is over 10MB in size.'.format(file.name)))

            try:
                Image.open(file).verify()
                file.seek(0)
            except Exception as e:
                raise forms.ValidationError(_('{} is not an appropriate image file, please select a JPEG or PNG.'.format(file.name)))

            im = Image.open(file)
            if im.format not in SUPPORTED_IMAGE_FORMATS:
                raise forms.ValidationError(_('{} is not a supported image type, please select a JPEG or PNG.'.format(file.name)))

        return file

    class Meta:
        model = User
        fields = ['full_name', 'language', 'avatar']

