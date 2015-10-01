from django.conf.urls import patterns, include, url

from django.contrib import admin
from apps.users import views as userviews
from .views import index, about
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
    url(r'^search/', include('apps.search.urls')),
    url(r'^faq/', include('apps.faq.urls')),
    url(r'^carpool/', include('apps.carpools.urls')),
    url(r'^about/$', about, name='about'),
    url(r'^$', index, name='index'),
)
