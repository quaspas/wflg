from django.conf.urls import patterns, url
from whatsforlunch.search.views import SearchView, SearchSimpleView


urlpatterns = patterns('',
        url(r'^/$',                  SearchSimpleView.as_view(), name='search.simple.form'),
        url(r'^/$',                  SearchView.as_view(), name='search.form'),
    )
