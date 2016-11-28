from django.conf.urls import url, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('Entrance', views.PlatycodonViewSet)


urlpatterns = [
    url(r'^rest/', include(router.urls))
]
