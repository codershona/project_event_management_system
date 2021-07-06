from django import forms

# from .models import Contributor

# class RegistrationForm(forms.ModelForm):
class RegistrationForm(forms.Form):
    email_address = forms.EmailField(label='Your email address')
    phone_number = forms.IntegerField(label='Please enter your phone number')
    # class Meta:
        # model = Contributor
        # fields = ['email_address', 'phone_number']