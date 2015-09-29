from django.conf.urls import patterns, url
import apps.users.views as userviews

urlpatterns = patterns(
    '',
    url(r'^settings/$', userviews.userSettings, name='userSettings'),
    url(r'^settings/changepassword/$', userviews.changePassword, name='changePassword'),
    url(r'^acquireInfo/$', userviews.acquireInfo, name='fetch_info'),
    # url(r'^resetpassword/', userviews.resetPasswordToken, name='resetPasswordToken'),
    # url(r'^forgetpassword/$', userviews.sendPasswdVrfCode, name='sendPasswdVrfCode'),
)
