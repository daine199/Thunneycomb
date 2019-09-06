#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path, include

from platycodon import views
from platycodon.admin import admin_site


urlpatterns = [
    path('platycodon-admin', admin_site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path("id/", views.get_platycodon_by_id, name='Platycodon Detail')
]


