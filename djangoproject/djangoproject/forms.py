from django import forms

class LoginForm(forms.Form):
    user = forms.CharField(label="Username", max_length=512)
    passcode = forms.CharField(label="Password", max_length=512)
