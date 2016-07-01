from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^login/$', views.login_processor, name='login_processor'),
    url(r'^logout/$', views.logout_processor, name='logout_processor')
]