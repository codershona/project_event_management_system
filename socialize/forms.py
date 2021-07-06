from django import forms

from .models import Contributor

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Contributor
        fields = ['email_address', 'phone_number']