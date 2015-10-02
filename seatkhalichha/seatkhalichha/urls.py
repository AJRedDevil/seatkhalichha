from django.conf.urls import patterns, include, url

from django.contrib import admin
from apps.users import views as userviews
from .views import index, about, fbpost
admin.autodiscover()

urlpatterns = patterns(
    '',
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^signin/$', userviews.signin, name='signin'),
    # url(r'^signup/$', userviews.signup, name='signup'),
    url(r'^logout/$', userviews.logout, name='logout'),
    url(r'^home/$', userviews.home, name='home'),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('apps.users.urls')),
    url(r'^feeds/', include('apps.collectors.urls')),
    url(r'^search/', include('apps.search.urls')),
    url(r'^faq/', include('apps.faq.urls')),
    url(r'^carpool/', include('apps.carpools.urls')),
    url(r'^about/$', about, name='about'),
    url(r'^29da3b71f7b34643a90ab1d7fd843df9/$', fbpost, name='fbpost'),
    url(r'^$', index, name='index'),
)
