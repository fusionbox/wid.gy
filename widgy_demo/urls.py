from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from .widgy_site import site as widgy_site

urlpatterns = patterns('',
    url(r'^$', 'mezzanine.pages.views.page', {'slug': '/'}, name='home'),

    url(r'^admin/widgy/', include(widgy_site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^widgy/', include('widgy.contrib.widgy_mezzanine.urls')),

    url(r'^', include('mezzanine.urls')),
)
