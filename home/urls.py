from django.conf.urls import url, include
from . import views
from rest_framework import routers


urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^logout/$', views.logout_processor, name='logout_processor')
]

urlpatterns += [
    url(r'^entrance/$', views.entrance_list),
    url(r'^entrance/(?P<pk>[0-9]+)/$', views.entrance_detail),
]

router = routers.DefaultRouter()
router.register('Entrance', views.EntranceViewSet)

urlpatterns += [
    url(r'^rest/', include(router.urls))
]
