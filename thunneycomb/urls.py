"""thunneycomb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include
from django.contrib import admin
from wiki.urls import get_pattern as get_wiki_pattern
from django_nyt.urls import get_pattern as get_nyt_pattern
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views
from rest_framework.authtoken import views as rest_views

admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.site_title = 'Thunneycomb'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls', namespace='home'))
]

urlpatterns += [
    url(r'^wiki/notifications/', get_nyt_pattern()),
    url(r'^wiki/', get_wiki_pattern())
]

urlpatterns += [
    url(r'^summerhere/', include('summerhere.urls', namespace='summerhere'))
]

urlpatterns += [
    url(r'^admin/login/$', views.login, name='login'),
    url(r'^admin/logout/$', views.logout, name='logout'),
    url(r'^admin/password_change/$', views.password_change, name='password_change'),
    url(r'^password_change/done/$', views.password_change_done, name='password_change_done'),
    url(r'^password_reset/$', views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', views.password_reset_complete, name='password_reset_complete'),
]

# REST LOGIN
if settings.LOGIN_ENABLE:
    urlpatterns += [
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        url(r'^api-token-auth/', rest_views.obtain_auth_token)
    ]




