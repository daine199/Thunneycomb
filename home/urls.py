from django.conf.urls import url
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^logout/$', views.logout_processor, name='logout_processor')
]

urlpatterns += static('/weimo/', document_root="/home/sophie.mao/www-root")
