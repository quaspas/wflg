from django.conf.urls import patterns, url
from whatsforlunch.account.views import AccountLoginView

from whatsforlunch.core.views import HomeView

urlpatterns = patterns('',
        url(r'^login/$',                  AccountLoginView.as_view(), name='account.login'),
    )
