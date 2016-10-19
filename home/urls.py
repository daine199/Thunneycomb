from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='homepage'),
#     url(r'^login/$', views.login_processor, name='login_processor'),
    url(r'^logout/$', views.logout_processor, name='logout_processor')
#
# ]
#
# # login test
# urlpatterns += [
#     url(r'^login_page/$', views.login_page, name='login_page'),
#     url(r'^login_test/$', views.login_test_page, name='login_test_page')
]