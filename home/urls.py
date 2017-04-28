from django.conf.urls import url, include
from . import view
from .views import common_api
from platycodon.views import PlatycodonViewSet
from rest_framework import routers


urlpatterns = [
    url(r'^$', view.entrance, name='entrance_page'),
    url(r'^account/login/$', view.login_user, name='login_page'),
    url(r'^logout/$', view.logout_processor, name='logout_processor')
]

urlpatterns += [
    url(r'^index/$', view.index, name='index_page'),
]

#  Deploy ROUTER
urlpatterns += [
    url(r'^deploy/$', view.deploy_entrance, name='deploy_entrance')
]

# REST ROUTER
router = routers.DefaultRouter()
router.register('HomeEntrance', view.EntranceViewSet)
router.register('PlatycodonEntrance', PlatycodonViewSet)

urlpatterns += [
    url(r'^rest/', include(router.urls))
]

# GET TEST
urlpatterns += [
    url(r'^get_session$', common_api.get_session, name='get_session'),
    url(r'^get_token$', common_api.get_token, name='get_token'),
    url(r'^token_test$', common_api.token_login, name='token_test'),
]
