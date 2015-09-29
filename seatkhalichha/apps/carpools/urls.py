from django.conf import settings
from django.conf.urls import patterns, include, url
# from django.contrib import admin
# admin.autodiscover()

from apps.carpools import views as carpoolviews

urlpatterns = patterns('',
    url(r'^$', carpoolviews.listAllCarpools, name='listAllCarpools'),
    url(r'^create/$', carpoolviews.createCarpool, name='createCarpool'),
    url(r'^request/(?P<carpool_id>\w+)', carpoolviews.requestCarpool, name='requestCarpool'),
    url(r'(?P<carpool_id>\w+)/$', carpoolviews.viewCarpool, name='viewCarpool' ),
)
