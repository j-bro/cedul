from django.conf.urls import patterns, url

from cedul_app import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^(?P<event_key>\d+)/$', views.event, name='event')
)