from django.contrib import admin
from .models import cmdTask, runLevel, winterUser
# Register your models here.

# class cmdTaskInline(admin.StackedInline):
#     model = cmdTask
#     extra = 3

class runLevelAdmin(admin.ModelAdmin):
    list_display = ('id','title','level')

class winterUserAdmin(admin.ModelAdmin):
    list_display = ('id','userid','runLevel','passwd')

class cmdTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'ownerid','cmd','runlevel')

admin.site.register(cmdTask, cmdTaskAdmin)
admin.site.register(winterUser, winterUserAdmin)
admin.site.register(runLevel, runLevelAdmin)