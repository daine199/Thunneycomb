from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import Entrance, Switch, UserProfile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Register your models here.


# 设置站点名
class MyAdminSite(AdminSite):
    site_header = 'Thunneycomb Admin'


admin_site = MyAdminSite(name='myadmin')


# 设置用户额外信息内嵌显示
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1
    can_delete = False
    verbose_name_plural = 'Ext Info'


class TokenInline(admin.StackedInline):
    model = Token
    max_num = 1
    can_delete = False
    verbose_name_plural = 'Rest Auth Token'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'phone_number', "is_staff")
    inlines = (UserProfileInline, TokenInline, )

    def phone_number(self, obj):
        return obj.userprofile.phone_number


class TokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'key')


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin_site.register(User, UserAdmin)
admin_site.register(Entrance)
admin_site.register(Switch)
admin_site.register(Token, TokenAdmin)


@admin.register(Entrance, Switch)
class HomeAdmin(admin.ModelAdmin):
    pass
