from django.conf.urls import url
from . import views
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', 'views.blog_list', name='blog_list')
]