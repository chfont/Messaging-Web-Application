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
    title= forms.CharField(label="Title", max_length=64, widget=forms.TextInput(attrs={'id':'forminput'}))
    key=forms.CharField(label="Key", max_length=64, required= False,widget=forms.PasswordInput(attrs={'id':'forminput'}))
    recipients=forms.CharField(label="Recipients", widget=forms.TextInput(attrs={'id':'forminput'}))



THEMES =[
    ("", "Select a Theme"),
    ("default", "Default"),
    ("light", "Light"),
    ("dark", "Dark")
]

SORT =[
    (0, "Recent"),
    (1, "Name(A-Z)"),
    (2, "Name(Z-A)"),
    (3, "Old")
]
class ThemeSelect(forms.Form):
    id = forms.CharField(label="Select Theme:", widget=forms.Select(choices=THEMES, attrs={'onchange': 'this.form.submit()', 'id':'formbutton'}))

class SortSelect(forms.Form):
    sortId = forms.CharField(widget=forms.Select(choices=SORT, attrs={'placeholder': 'Select', 'onclick': 'this.form.submit();', 'id':'formbutton'}))

class ConvEnter(forms.Form):
    convID = forms.CharField(widget=forms.HiddenInput())
    key = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'forminput'}), required = False)
