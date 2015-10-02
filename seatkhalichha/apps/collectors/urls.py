from django.conf import settings
from django.conf.urls import patterns, include, url
# from django.contrib import admin
# admin.autodiscover()

from apps.collectors import views as feedviews

urlpatterns = patterns(
    '',
    url(r'^$', feedviews.listAllFeeds, name='listAllFeeds'),
    url(r'(?P<feed_id>\w+)/$', feedviews.viewFeed, name='viewFeed'),
)
