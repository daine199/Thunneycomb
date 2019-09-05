from django.contrib import admin
from .forms import PlatycodonAdminForm
from .models import Platycodon, PlatycodonTag
from django.contrib.admin import AdminSite


# Register your models here.
class PlatycodonAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'tag_list']
    form = PlatycodonAdminForm

    def tag_list(self, obj):
        tag_lists = []
        tags = PlatycodonTag.objects.filter(platycodon_id=obj.id)
        if len(tags) < 1:
            return "-- No Tag --"
        else:
            for tag in tags:
                tag_lists.append(tag.tag_name)
        return tag_lists


class PlatycodonTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'platycodon_title', 'tag_name']

    def platycodon_title(self, obj):
        if obj.platycodon_id is 0:
            return "-- Empty --"
        platycodon = Platycodon.objects.get(id=obj.platycodon_id)
        return platycodon.title


# 设置站点名
class PlatycodonAdminSite(AdminSite):
    site_header = 'Platycodon Admin'


admin_site = PlatycodonAdminSite(name='Platycodon Admin')

admin_site.register(Platycodon, PlatycodonAdmin)
admin_site.register(PlatycodonTag, PlatycodonTagAdmin)
