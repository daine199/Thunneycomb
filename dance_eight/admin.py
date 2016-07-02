from django.contrib import admin
from django import forms
from redactor.widgets import RedactorEditor
from .models import Article


class ArticleAdminForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = (
            'title',
            'author',
            'content'
        )
        widgets = {
           'content': RedactorEditor(),
        }


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    form = ArticleAdminForm


admin.site.register(Article, ArticleAdmin)