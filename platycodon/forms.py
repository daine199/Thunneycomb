from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Platycodon


class PlatycodonAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Platycodon
        fields = ['title', 'author']

