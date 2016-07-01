from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^delay_test/$', views.performance_in, name='performance_in'),
    url(r'^delay_test/(?P<delay>[0-9]+)/$', views.performance_in, name='performance_in_set')
]