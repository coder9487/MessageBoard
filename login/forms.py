from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=100,widget=forms.PasswordInput)
    file = forms.FileField()
