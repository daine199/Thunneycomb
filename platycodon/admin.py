from django.contrib import admin
from .forms import PlatycodonAdminForm
from .models import Platycodon

# Register your models here.


class PlatycodonAdmin(admin.ModelAdmin):
    list_display = ['title']
    form = PlatycodonAdminForm

admin.site.register(Platycodon, PlatycodonAdmin)
