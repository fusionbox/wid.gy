from django.conf.urls import patterns, url
from marketing.views import home

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
)
