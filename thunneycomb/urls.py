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
from django.conf.urls import url, include
from django.contrib import admin
from wiki.urls import get_pattern as get_wiki_pattern
from django_nyt.urls import get_pattern as get_nyt_pattern

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls', namespace='home'))

]

urlpatterns += [
    url(r'^wiki/notifications/', get_nyt_pattern()),
    url(r'^wiki/', get_wiki_pattern())
]

urlpatterns += [
    url(r'^summerhere/', include('summerhere.urls', namespace='summerhere')),
    url(r'^wintercome/', include('wintercome.urls', namespace='wintercome')),
    url(r'^dance_eight/', include('dance_eight.urls', namespace='dance_eight'))
]