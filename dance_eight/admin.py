from django.contrib import admin
from django import forms
from redactor.widgets import RedactorEditor
from .models import Article, Comment


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


class CommentAdminForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'target',
            'content'
        )
        widgets = {
            'content': RedactorEditor(),
        }


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    form = ArticleAdminForm


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'target', 'content')
    form = CommentAdminForm


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)