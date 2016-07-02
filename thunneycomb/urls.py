from django.conf.urls import url, include
from django.contrib import admin
from wiki.urls import get_pattern as get_wiki_pattern
from django_nyt.urls import get_pattern as get_nyt_pattern
from django.conf import settings
from django.conf.urls.static import static
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


# 默认admin 入口
urlpatterns = [
    url(r'^admin/', admin.site.urls)
]

# 主页入口
urlpatterns += [
    url(r'^', include('home.urls', namespace='home'))
]

# wiki 入口
urlpatterns += [
    url(r'^wiki/notifications/', get_nyt_pattern()),
    url(r'^wiki/', get_wiki_pattern())
]

# thunneycomb 入口
urlpatterns += [
    url(r'^summerhere/', include('summerhere.urls', namespace='summerhere')),
    url(r'^wintercome/', include('wintercome.urls', namespace='wintercome')),
    url(r'^dance_eight/', include('dance_eight.urls', namespace='dance_eight')),
    url(r'^redactor/', include('redactor.urls'))
]

# Media DEBUG环境静态链接入口, 如果生产环境,需要通过nginx或其他http服务器配置静态地址。
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
