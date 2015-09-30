from django.conf.urls import patterns, url
import apps.search.views as searchviews

urlpatterns = patterns(
    '',
    url(r'^$', searchviews.carpoolSearch, name='carpoolSearch'),
    url(r'carpools/$', searchviews.carpoolSearchDetail, name='carpoolSearchDetail'),
)
