from django.conf.urls import patterns, url

from cedul_app import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^event_redirect/', views.event_redirect, name='event_redirect'),
    url(r'^create_event/', views.create_event, name='create_event'),
    url(r'^(?P<public_key>\w+)/$', views.event, name='event')
)