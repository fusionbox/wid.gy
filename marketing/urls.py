from django.conf.urls import url
from marketing.views import home

urlpatterns = [
    url(r'^$', home, name='home'),
]
