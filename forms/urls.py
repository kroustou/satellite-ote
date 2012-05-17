#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import ParticipationView, thanks

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', ParticipationView.as_view()),
    url(r'^thanks$', thanks, name='thank_you')
    # url(r'^nemeaform/', include('nemeaform.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
