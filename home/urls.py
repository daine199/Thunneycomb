from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^logout/$', views.logout_processor, name='logout_processor')
]


