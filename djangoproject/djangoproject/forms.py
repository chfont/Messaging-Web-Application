from django import forms

class LoginForm(forms.Form):
    user = forms.CharField(label="Email", max_length=512)
    passcode = forms.CharField(label="Password", max_length=512, widget=forms.PasswordInput)

class NewUser(forms.Form):
    email = forms.CharField(label="Recovery Email", max_length=512)
    username = forms.CharField(label="Username", max_length=512)
    password = forms.CharField(label="Password", max_length=512, widget=forms.PasswordInput)
    confirmPassword = forms.CharField(label="Confirm Password", max_length=512, widget=forms.PasswordInput)

class NewConv(forms.Form):
    title= forms.CharField(label="Title", max_length=64)
    key=forms.CharField(label="Key", max_length=64, required= False,widget=forms.PasswordInput)


THEMES =[
    ("default", "Default"),
    ("light", "Light"),
    ("dark", "Dark")
]
class ThemeSelect(forms.Form):
    id = forms.CharField(label="Select Theme:", widget=forms.Select(choices=THEMES))
