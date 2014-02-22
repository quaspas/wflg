from django.conf.urls import patterns, include, url

from whatsforlunch.core.views import HomeView
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
     url(r'^$', HomeView.as_view(), name='home'),

     url(r'^account/', include('whatsforlunch.account.urls')),
)
