from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Platycodon
from django.contrib.auth.models import User


class PlatycodonAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Platycodon
        fields = ['title']


