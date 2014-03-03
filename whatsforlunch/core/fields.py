from django import forms


class EmailField(forms.EmailField):

    def clean(self, value):
        value = self.to_python(value).strip().lower()
        return super(EmailField, self).clean(value)