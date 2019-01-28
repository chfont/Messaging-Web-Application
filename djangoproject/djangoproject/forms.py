from django import forms

class LoginForm(forms.Form):
    user = forms.CharField(label="Username", max_length=512)
    passcode = forms.CharField(label="Password", max_length=512, widget=forms.PasswordInput)

class NewUser(forms.Form):
    user = forms.CharField(label="Username", max_length=512)
    password = forms.CharField(label="Password", max_length=512, widget=forms.PasswordInput)
    confirmPassword = forms.CharField(label="Confirm Password", max_length=512, widget=forms.PasswordInput)
    recovEmail = forms.CharField(label="Recovery Email", max_length=512)
