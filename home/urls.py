from django.conf.urls import url, include
from . import views
from platycodon.views import PlatycodonViewSet
from rest_framework import routers


urlpatterns = [
    url(r'^$', views.entrance, name='entrance_page'),
    url(r'^account/login/$', views.login_user, name='login_page'),
    url(r'^logout/$', views.logout_processor, name='logout_processor')
]

urlpatterns += [
    url(r'^index/$', views.index, name='index_page'),
]

#  Deploy ROUTER
urlpatterns += [
    url(r'^deploy/$', views.deploy_entrance, name='deploy_entrance')
]

# REST ROUTER
router = routers.DefaultRouter()
router.register('HomeEntrance', views.EntranceViewSet)
router.register('PlatycodonEntrance', PlatycodonViewSet)

urlpatterns += [
    url(r'^rest/', include(router.urls))
]

# logging test
urlpatterns += [
    url(r'^logging$', views.my_view)
]

