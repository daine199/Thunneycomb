from django.contrib import admin
from .models import DanceEightManager, Tag, Classification, Author, Article
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'website')
    search_fields = ('name',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'classification', 'author', 'publish_time', 'update_time')
    list_filter = ('publish_time',)
    date_hierarchy = 'publish_time'
    ordering = ('-publish_time',)
    filter_horizontal = ('tags',)

admin.site.register(DanceEightManager)
admin.site.register(Tag)
admin.site.register(Classification)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)