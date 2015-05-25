# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^(?P<topic_id>\d+)/create/$', views.favorite_create, name='favorite-create'),
    url(r'^(?P<pk>\d+)/delete/$', views.favorite_delete, name='favorite-delete'),
]