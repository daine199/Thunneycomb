# Owner Daine.H
# Modify 2016-01-05

from django import forms


class UserLogin(forms.Form):
    userid = forms.CharField(label='User ID', max_length=32)
    passwd = forms.CharField(label='Password', widget=forms.PasswordInput())
