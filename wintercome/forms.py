# Owner Daine.H
# Modify 2016-01-05

from django import forms


class UserLogin(forms.Form):
    userid = forms.CharField(label='User ID', max_length=32, widget=forms.TextInput(attrs={"class":"form-control","placeholder":"UserID"}))
    passwd = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))
