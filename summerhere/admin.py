from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from .models import Summer, SummerImage

# Register your models here.


class SummerAdminForm(forms.ModelForm):
    title = forms.CharField(max_length=120)
    owner = forms.CharField(max_length=30)
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Summer
        fields = ['title', 'owner', 'content',]


class SummerImageAdminForm(forms.ModelForm):
    class Meta:
        model = SummerImage
        fields = ['id', 'img_description', 'artical_belong', 'img']


class SummerImageInline(admin.TabularInline):
    model = SummerImage


class SummerAdmin(admin.ModelAdmin):
    form = SummerAdminForm
    inlines = [
        SummerImageInline
    ]


class SummerImageAdmin(admin.ModelAdmin):
    form = SummerImageAdminForm

admin.site.register(Summer, SummerAdmin)
admin.site.register(SummerImage, SummerImageAdmin)
